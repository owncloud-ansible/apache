---
title: apache
type: docs
---

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/owncloud-ansible/apache) [![Build Status](https://drone.owncloud.com/api/badges/owncloud-ansible/apache/status.svg)](https://drone.owncloud.com/owncloud-ansible/apache) [![GitHub](https://img.shields.io/github/license/owncloud-ansible/apache)](https://github.com/owncloud-ansible/apache/blob/master/LICENSE) 

{{< hint warning >}} __Warning__<br/> This Ansible role is currently in beta state. Use it at your own risk. {{< /hint >}} 

Role to setup Apache webserver.

* [Default Variables](#default-variables)
  * [apache_allow_override](#apache-allow-override)
  * [apache_apt_cache_update](#apache-apt-cache-update)
  * [apache_listen_ip](#apache-listen-ip)
  * [apache_listen_port](#apache-listen-port)
  * [apache_listen_port_ssl](#apache-listen-port-ssl)
  * [apache_mods_disabled](#apache-mods-disabled)
  * [apache_mods_enabled](#apache-mods-enabled)
  * [apache_options](#apache-options)
  * [apache_packages_extra](#apache-packages-extra)
  * [apache_packages_state](#apache-packages-state)
  * [apache_restart_state](#apache-restart-state)
  * [apache_ssl_cipher_suite](#apache-ssl-cipher-suite)
  * [apache_ssl_protocol](#apache-ssl-protocol)
  * [apache_state](#apache-state)
  * [apache_vhost_name](#apache-vhost-name)
  * [apache_vhosts](#apache-vhosts)
  * [apache_vhosts_ssl](#apache-vhosts-ssl)
* [Dependencies](#dependencies)

---

## Default Variables

### apache_allow_override

#### Default value

```YAML
apache_allow_override: All
```

### apache_apt_cache_update

Automatically update apt cache on package installations. This setting will only applied on apt-based operating systems e.g. Ubuntu.

#### Default value

```YAML
apache_apt_cache_update: false
```

### apache_listen_ip

#### Default value

```YAML
apache_listen_ip: '*'
```

### apache_listen_port

#### Default value

```YAML
apache_listen_port: 80
```

### apache_listen_port_ssl

#### Default value

```YAML
apache_listen_port_ssl: 443
```

### apache_mods_disabled

#### Default value

```YAML
apache_mods_disabled: []
```

### apache_mods_enabled

Only used on Debian/Ubuntu.

#### Default value

```YAML
apache_mods_enabled:
  - rewrite.load
  - ssl.load
  - headers.load
  - env.load
  - dir.load
  - mime.load
  - unique_id.load
  - autoindex.load
```

### apache_options

#### Default value

```YAML
apache_options:
  - -Indexes
  - +FollowSymLinks
```

### apache_packages_extra

Can be used to install other dependency packages.

#### Default value

```YAML
apache_packages_extra: []
```

### apache_packages_state

Use `present` to make sure it's installed, or `latest` if you want to upgrade.

#### Default value

```YAML
apache_packages_state: present
```

### apache_restart_state

Set apache state when configuration changes are made. Recommended values: `restarted` or `reloaded`.

#### Default value

```YAML
apache_restart_state: restarted
```

### apache_ssl_cipher_suite

#### Default value

```YAML
apache_ssl_cipher_suite: AES256+EECDH:AES256+EDH
```

### apache_ssl_protocol

#### Default value

```YAML
apache_ssl_protocol: All -SSLv2 -SSLv3
```

### apache_state

Set initial apache state. Recommended values: `started` or `stopped`.

#### Default value

```YAML
apache_state: started
```

### apache_vhost_name

#### Default value

```YAML
apache_vhost_name: owncloud.conf
```

### apache_vhosts

#### Default value

```YAML
apache_vhosts:
  - servername: cloud.owncloud.demo
    documentroot: /var/www/owncloud
```

### apache_vhosts_ssl

#### Default value

```YAML
apache_vhosts_ssl: []
```

#### Example usage

```YAML
apache_vhosts_ssl:
  - servername: "local.dev"
    documentroot: "/var/www/html"
    certificate_file: "/path/to/certificate.crt"
    certificate_file_source: "/path/to/source/on/ansible_host/certificate.crt"
    certificate_key_file: "/path/to/certificate.key"
    certificate_key_source: "/path/to/source/on/ansible_host/certificate.key"
    # Optional.
    certificate_chain_file: "/path/to/certificate_chain.crt"
    certificate_chain_source: "/path/to/source/on/ansible_host/certificate_chain.crt"
    header_ocsp_trusted_certificate:
    header_hsts_options:
      - max-age=63072000
      - includeSubDomains
    header_xfo_policy: deny
    header_xcto_enabled: True
    header_csp_options:
      - directive: frame-ancestors
        parameters:
          - https://example.com
          - https://mypage.com
    header_xxxsp_parameters:
      - mode=block
```

## Dependencies

None.
