#!/usr/bin/env python3
import os
from os.path import expanduser
import hvac
import sys
import getpass

vault_addr = os.getenv('VAULT_ADDR')

def _check_aws_cli():
  home = expanduser("~")
  awsconfigfile = os.path.exists(home + '/.aws/config') 
  awscredsfile = os.path.exists(home + '/.aws/credentials')
  if awsconfigfile == True & awscredsfile == True:
    _check_vault_addr()
  else:
    print("\nAWS CLI not installed or not configured. \nhttps://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html \n")
    sys.exit(1)

def _check_vault_addr():
  if vault_addr == None:
    print("VAULT_ADDR is not set. Use 'export VAULT_ADDR=https://1.2.3.4:8200/'")
    sys.exit(1)
  else:
    _vaultcreds()

def _usercreds():
  USERNAME = input("Enter your username: ")
  PASSWORD = getpass.getpass("Enter your password: ")
  return USERNAME, PASSWORD

def _vaultcreds():
  user = _usercreds()
  USER = (user[0])
  PASS = (user[1])
  try:
    client = hvac.Client(url=vault_addr)
    client.auth_userpass(USER, PASS)
    list_roles_response = client.secrets.aws.list_roles(mount_point='customaws')
    list_user_roles = list_roles_response['data']['keys']
    length = len(list_user_roles)
    for i in range(length):
      print("ROLE: " + list_user_roles[i] + " - available ")
    role = input("Type the role to use: ")
    gen_creds_response = client.secrets.aws.generate_credentials(name=role.strip(), mount_point='customaws')
    access=gen_creds_response['data']['access_key']
    secret=gen_creds_response['data']['secret_key']
    print("Generated access / secret keys:\n" +
      "\nexport AWS_ACCESS_KEY_ID=" + access +
      "\nexport AWS_SECRET_ACCESS_KEY=" + secret )
  except Exception as e:
    print(str(e))

if __name__=="__main__":
  _check_aws_cli()
