# tcld migration command reference

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> (private preview) Manage migrations between self-hosted Temporal and Temporal cloud

`tcld migration`: (private preview) Manage migrations between self-hosted Temporal and Temporal cloud.

Alias: `m`

- [tcld migration get](#get)
- [tcld migration list](#list)
- [tcld migration start](#start)
- [tcld migration handover](#handover)
- [tcld migration confirm](#confirm)
- [tcld migration abort](#abort)

### get

`tcld migration get`: Get a migration.

Alias: `g`

#### --id

Migration id

Alias: `i`

### list

`tcld migration list`: List migrations.

Alias: `l`

### start

`tcld migration start`: Start a new migration.

Alias: `s`

#### --request-id

The request-id to use for the asynchronous operation, if not set the server will assign one (optional)

Alias: `r`

#### --endpoint-id

Migration endpoint id

Alias: `e`

#### --source-namespace

Source namespace name

Alias: `s`

#### --target-namespace

Target namespace name

Alias: `t`

### handover

`tcld migration handover`: Handover the namespace from on-prem to cloud, or from cloud back to on-prem.

Alias: `s`

#### --request-id

The request-id to use for the asynchronous operation, if not set the server will assign one (optional)

Alias: `r`

#### --id

Migration id

Alias: `i`

#### --to-replica-id

The id of the replica to make active

Alias: `rp`

### confirm

`tcld migration confirm`: Confirm the migration.

Alias: `c`

#### --request-id

The request-id to use for the asynchronous operation, if not set the server will assign one (optional)

Alias: `r`

#### --id

Migration id

Alias: `i`

### abort

`tcld migration abort`: Abort the migration.

Alias: `a`

#### --request-id

The request-id to use for the asynchronous operation, if not set the server will assign one (optional)

Alias: `r`

#### --id

Migration id

Alias: `i`
