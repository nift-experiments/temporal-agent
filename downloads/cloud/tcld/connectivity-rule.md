# tcld connectivity-rule command reference

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Connectivity rule operations

`tcld connectivity-rule`: Connectivity rule operations.

Alias: `cr`

- [tcld connectivity-rule create](#create)
- [tcld connectivity-rule get](#get)
- [tcld connectivity-rule list](#list)
- [tcld connectivity-rule delete](#delete)

### create

`tcld connectivity-rule create`: Create a connectivity rule.

Alias: `c`

#### --connectivity-type

The type of connectivity, currently only support 'private' and 'public'

Alias: `ct`

#### --connection-id

The connection ID of the private connection

Alias: `ci`

#### --region

The region of the connection

Alias: `r`

#### --gcp-project-id

The GCP project ID of the connection, required if the cloud provider is 'gcp'

Alias: `gpi`

### get

`tcld connectivity-rule get`: Get a connectivity rule.

Alias: `g`

#### --connectivity-rule-id

The connectivity rule ID

Alias: `id`

### list

`tcld connectivity-rule list`: list connectivity rules.

Alias: `l`

#### --namespace

The namespace hosted on temporal cloud

Alias: `n`

### delete

`tcld connectivity-rule delete`: Delete a connectivity rule.

Alias: `d`

#### --connectivity-rule-id

The connectivity rule ID

Alias: `id`
