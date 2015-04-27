## Link Shortener

Quick link shortener for an interview prep session

To install:
`git clone` this repo
`vagrant up` from repo directory

Dependencies: git, vagrant

If you want to use with Amazon AWS, add your credentials to your local environment variables:
export AWS_ACCESS_KEY="FILL THIS IN"
export AWS_SECRET_KEY="FILL THIS IN"
export AWS_KEYPAIR_NAME="FILL THIS IN"
export AWS_KEYPAIR_PRIVATEKEY_PATH="FILL THIS IN"

Make sure the user you create has access to create EC2 instances.

Then instead of `vagrant up` , type `vagrant up --provider=aws`

Lots to do:
- Add persistence
- Add error checking / validation
- Don't require http://