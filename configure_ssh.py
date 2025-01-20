#!/usr/bin/env python3

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

def configure_ssh(task):
    domain_name = task.host.get("data", {}).get("domain_name", "cisco.com")
    new_hostname = task.host.name
    management_ip = task.host.get("data", {}).get("management_ip", None)
    management_interface = task.host.get("data", {}).get("management_interface", None)
    management_mask = task.host.get("data", {}).get("management_mask", None)

    config_cmds = [
        f"hostname {new_hostname}",
        f"ip domain-name {domain_name}",
        "crypto key generate rsa modulus 1024",
        "enable secret admin",
        "line vty 0 4",
        "transport input telnet ssh",
        "login local",
        "exit",
        "username admin secret admin"
    ]


    if management_ip and management_interface and management_mask:
        config_cmds.extend([
            f"interface {management_interface}",
            f"ip address {management_ip} {management_mask}",
            "no shutdown"
        ])
    elif management_ip or management_interface or management_mask:
        task.results["error"] = (
            "Incomplete management configuration: management_ip, management_interface, and management_mask must all be defined together. "

        )

    result = task.run(
        task=netmiko_send_config,
        config_commands=config_cmds
    )
    return result

def main():
    nr = InitNornir(config_file="nornir.yaml")
    result = nr.run(task=configure_ssh)
    print_result(result)

if __name__ == "__main__":
    main()

