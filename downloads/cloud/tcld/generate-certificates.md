# tcld generate-certificates command reference

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Commands for generating certificate authority and end-entity TLS certificates

`tcld generate-certificates`: Commands for generating certificate authority and end-entity TLS certificates.

Alias: `gen`

- [tcld generate-certificates certificate-authority-certificate](#certificate-authority-certificate)
- [tcld generate-certificates end-entity-certificate](#end-entity-certificate)

### certificate-authority-certificate

`tcld generate-certificates certificate-authority-certificate`: Generate a certificate authority certificate.

Alias: `ca`

#### --organization

The name of the organization

Alias: `org`

#### --validity-period

The duration for which the certificate is valid for. example: 30d10h (30 days and 10 hrs)

Alias: `d`

#### --ca-certificate-file

The path where the generated x509 certificate will be stored

Alias: `ca-cert`

#### --ca-key-file

The path where the certificate's private key will be stored

Alias: `ca-key`

#### --rsa-algorithm

Generates a 4096-bit RSA keypair instead of an ECDSA P-384 keypair (the recommended default) for the certificate (optional)

Alias: `rsa`

### end-entity-certificate

`tcld generate-certificates end-entity-certificate`: Generate an end-entity certificate.

Alias: `leaf`

#### --organization

The name of the organization

Alias: `org`

#### --organization-unit

The name of the organizational unit (optional)

#### --common-name

The common name (optional)

#### --validity-period

The duration for which the end entity certificate is valid for. example: 30d10h (30 days and 10 hrs). By default the generated certificate expires 24 hours before the certificate authority expires (optional)

Alias: `d`

#### --ca-certificate-file

The path of the x509 certificate for the certificate authority

Alias: `ca-cert`

#### --ca-key-file

The path of the private key for the certificate authority

Alias: `ca-key`

#### --certificate-file

The path where the generated x509 certificate will be stored

Alias: `cert`

#### --key-file

The path where the certificate's private key will be stored

Alias: `key`
