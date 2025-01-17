#!/usr/bin/env python3

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

def configure_ssh(task):
    domain_name = task.host.get("data", {}).get("domain_name", "cisco.com")
    new_hostname = task.host.name

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
