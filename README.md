<p align="center">
  <a href="https://www.cloud42.io/" target="_blank" rel="Homepage">
  <img width="200" height="200" src="https://www.cloud42.io/wp-content/uploads/2020/01/transparent_small.png">
  </a>
</p>

---
<p align="center">Need help with your Cloud builds <a href="https://www.cloud42.io/contact/" target="_blank" rel="ContactUS"> DROP US A LINE</a>.</p>

---
Python3 script. Authenticates against a Hashicorp Vault endpoint using username and password. Returns an access key and secret key.

#### Requirements

| Name | Version |
|------|---------|
| Python | >= 3.6.8 |

#### Add as a global command

* git clone git@github.com:Cloud-42/vault\_userpass\_util.git
* cd vault\_userpass\_util/
* sudo cp VaultGrabKeyPair.py /usr/local/bin/VaultGrab ( /usr/local/bin or a location in $PATH )

#### Using access key and secret key
The following will be returned if authentication is successful:

* export AWS\_ACCESS\_KEY\_ID=ABCDEFGHILCZRG2MLYYS
* export AWS\_SECRET\_ACCESS\_KEY=aBCY/YTHJko1XXBfnLJEFNL8IHwhZk/hlFwcgzaHX

Running these as is will add the access key and secret key for the current session. Adding the value to ~/.bashrc and running -> source ~/.bashrc -> will add to all bash sessions. The key pair can be added to an aws cli profile by running -> aws configure --profile=PROFILE\_NAME.

