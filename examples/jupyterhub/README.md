This example demonstrates how to deploy a single-host JupyterHub environment using Docker.

## Prerequisites

* [Docker Engine](https://docs.docker.com/engine/) 1.10.0+
* [Docker Machine](https://docs.docker.com/machine/) 0.6.0+
* [Docker Compose](https://docs.docker.com/compose/) 1.6.0+

See the [installation instructions](https://docs.docker.com/engine/installation/) for your environment.

## Quickstart

```
# activate the target docker machine
eval "$(docker-machine env mymachine)"
```

Get an SSL certificate chain from [Let's Encrypt](https://letsencrypt.org). (Skip this step if you already have SSL certificate chain and keys).

```
FQDN=host.mydomain.com EMAIL=myemail@somewhere.com \
  SECRETS_VOLUME=jupyterhub-secrets \
  ./letsencrypt.sh
```

We use GitHub for authenticating users, so register JupyterHub as a [new application](https://github.com/settings/applications/new).

Setup environment (TODO: add scripts with default values).

```
export SECRETS_VOLUME=jupyterhub-secrets
export GITHUB_CLIENT_ID=<client_id>
export GITHUB_CLIENT_SECRET=<client_secret>
export OAUTH_CALLBACK_URL=https://<host.mydomain.com>/hub/oauth_callback
```

Edit `userlist`.

Build hub image.

```
./build.sh
```

Start.

```
docker-compose -f jupyterhub.yml up -d
```
