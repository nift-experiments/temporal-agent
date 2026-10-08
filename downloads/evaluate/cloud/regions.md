# Service regions

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> The AWS and GCP regions where you can create a Temporal Cloud Namespace, and how region choice affects latency between your Workers and the Service.

You can reach Temporal Cloud from anywhere with Internet connectivity, wherever your Namespaces are located, and your applications can run in the cloud environment or data center of your choice.
Create Namespaces in a region close to where you host your Workers to reduce latency.

This page lists the regions where you can create a Temporal Cloud Namespace.

> **💡 Tip:**
> Service availability
>
> Check the status of supported regions at [status.temporal.io](https://status.temporal.io).
> Subscribe there to get an email whenever Temporal creates, updates, or resolves an incident.
>

## AWS service regions

Temporal Cloud operates in the following Amazon Web Services (AWS) regions:

### Asia Pacific - Tokyo (`ap-northeast-1`)

- **Cloud API Code**: `aws-ap-northeast-1`
- **Regional Endpoint**: `ap-northeast-1.aws.api.temporal.io:7233`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.ap-northeast-1.vpce-svc-08f34c33f9fb8a48a`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-ap-northeast-2`
  - `aws-ap-south-1`
  - `aws-ap-south-2`
  - `aws-ap-southeast-1`
  - `aws-ap-southeast-2`
- **Multi-Cloud Replication**:
  - `gcp-asia-south1`

### Asia Pacific - Seoul (`ap-northeast-2`)

- **Cloud API Code**: `aws-ap-northeast-2`
- **Regional Endpoint**: `ap-northeast-2.aws.api.temporal.io:7233`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.ap-northeast-2.vpce-svc-08c4d5445a5aad308`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-ap-northeast-1`
  - `aws-ap-south-1`
  - `aws-ap-south-2`
  - `aws-ap-southeast-1`
  - `aws-ap-southeast-2`
- **Multi-Cloud Replication**:
  - `gcp-asia-south1`

### Asia Pacific - Mumbai (`ap-south-1`)

- **Cloud API Code**: `aws-ap-south-1`
- **Regional Endpoint**: `ap-south-1.aws.api.temporal.io:7233`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.ap-south-1.vpce-svc-0ad4f8ed56db15662`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-ap-northeast-1`
  - `aws-ap-northeast-2`
  - `aws-ap-south-2`
  - `aws-ap-southeast-1`
  - `aws-ap-southeast-2`
- **Multi-Cloud Replication**:
  - `gcp-asia-south1`

### Asia Pacific - Hyderabad (`ap-south-2`)

- **Cloud API Code**: `aws-ap-south-2`
- **Regional Endpoint**: `ap-south-2.aws.api.temporal.io:7233`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.ap-south-2.vpce-svc-08bcf602b646c69c1`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-ap-northeast-1`
  - `aws-ap-northeast-2`
  - `aws-ap-south-1`
  - `aws-ap-southeast-1`
  - `aws-ap-southeast-2`
- **Multi-Cloud Replication**:
  - `gcp-asia-south1`

### Asia Pacific - Singapore (`ap-southeast-1`)

- **Cloud API Code**: `aws-ap-southeast-1`
- **Regional Endpoint**: `ap-southeast-1.aws.api.temporal.io:7233`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.ap-southeast-1.vpce-svc-05c24096fa89b0ccd`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-ap-northeast-1`
  - `aws-ap-northeast-2`
  - `aws-ap-south-1`
  - `aws-ap-south-2`
  - `aws-ap-southeast-2`
- **Multi-Cloud Replication**:
  - `gcp-asia-south1`

### Asia Pacific - Sydney (`ap-southeast-2`)

- **Cloud API Code**: `aws-ap-southeast-2`
- **Regional Endpoint**: `ap-southeast-2.aws.api.temporal.io:7233`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.ap-southeast-2.vpce-svc-0634f9628e3c15b08`
- **Same Region Replication**: Available
- **Multi-Region Replication**:
  - `aws-ap-northeast-1`
  - `aws-ap-northeast-2`
  - `aws-ap-south-1`
  - `aws-ap-south-2`
  - `aws-ap-southeast-1`
- **Multi-Cloud Replication**:
  - `gcp-asia-south1`

### Europe - Frankfurt (`eu-central-1`)

- **Cloud API Code**: `aws-eu-central-1`
- **Regional Endpoint**: `eu-central-1.aws.api.temporal.io:7233`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.eu-central-1.vpce-svc-073a419b36663a0f3`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-eu-west-1`
  - `aws-eu-west-2`
- **Multi-Cloud Replication**:
  - `gcp-europe-west3`

### Europe - Ireland (`eu-west-1`)

- **Cloud API Code**: `aws-eu-west-1`
- **Regional Endpoint**: `eu-west-1.aws.api.temporal.io:7233`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.eu-west-1.vpce-svc-04388e89f3479b739`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-eu-central-1`
  - `aws-eu-west-2`
- **Multi-Cloud Replication**:
  - `gcp-europe-west3`

### Europe - London (`eu-west-2`)

- **Cloud API Code**: `aws-eu-west-2`
- **Regional Endpoint**: `eu-west-2.aws.api.temporal.io:7233`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.eu-west-2.vpce-svc-0ac7f9f07e7fb5695`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-eu-central-1`
  - `aws-eu-west-1`
- **Multi-Cloud Replication**:
  - `gcp-europe-west3`

### North America - Central Canada (`ca-central-1`)

- **Cloud API Code**: `aws-ca-central-1`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.ca-central-1.vpce-svc-080a781925d0b1d9d`
- **Regional Endpoint**: `ca-central-1.aws.api.temporal.io:7233`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-us-east-1`
  - `aws-us-east-2`
  - `aws-us-west-2`
- **Multi-Cloud Replication**:
  - `gcp-us-central1`
  - `gcp-us-west1`
  - `gcp-us-east4`

### North America - Northern Virginia (`us-east-1`)

- **Cloud API Code**: `aws-us-east-1`
- **Regional Endpoint**: `us-east-1.aws.api.temporal.io:7233`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.us-east-1.vpce-svc-0822256b6575ea37f`
- **Same Region Replication**:  Available
- **Multi-Region Replication**:
  - `aws-ca-central-1`
  - `aws-us-east-2`
  - `aws-us-west-2`
- **Multi-Cloud Replication**:
  - `gcp-us-central1`
  - `gcp-us-west1`
  - `gcp-us-east4`

### North America - Ohio (`us-east-2`)

- **Cloud API Code**: `aws-us-east-2`
- **Regional Endpoint**: `us-east-2.aws.api.temporal.io:7233`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.us-east-2.vpce-svc-01b8dccfc6660d9d4`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `aws-ca-central-1`
  - `aws-us-east-1`
  - `aws-us-west-2`
- **Multi-Cloud Replication**:
  - `gcp-us-central1`
  - `gcp-us-west1`
  - `gcp-us-east4`

### North America - Oregon (`us-west-2`)

- **Cloud API Code**: `aws-us-west-2`
- **Regional Endpoint**: `us-west-2.aws.api.temporal.io:7233`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.us-west-2.vpce-svc-0f44b3d7302816b94`
- **Same Region Replication**:  Available
- **Multi-Region Replication**:
  - `aws-ca-central-1`
  - `aws-us-east-1`
  - `aws-us-east-2`
- **Multi-Cloud Replication**:
  - `gcp-us-central1`
  - `gcp-us-west1`
  - `gcp-us-east4`

### South America - São Paulo (`sa-east-1`)

- **Cloud API Code**: `aws-sa-east-1`
- **Regional Endpoint**: `sa-east-1.aws.api.temporal.io:7233`
- **PrivateLink Endpoint Service**: `com.amazonaws.vpce.sa-east-1.vpce-svc-0ca67a102f3ce525a`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - None
- **Multi-Cloud Replication**:
  - None

## GCP service regions

Temporal Cloud operates in the following Google Cloud (GCP) regions:

### North America - Iowa (`us-central1`)

- **Cloud API Code**: `gcp-us-central1`
- **Regional Endpoint**: `us-central1.gcp.api.temporal.io:7233`
- **Private Service Connect Service Attachment URI**: `projects/prod-d9ch6v2ybver8d2a8fyf7qru9/regions/us-central1/serviceAttachments/pl-5xzng`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `gcp-us-west1`
  - `gcp-us-east4`
- **Multi-Cloud Replication**:
  - `aws-ca-central-1`
  - `aws-us-east-1`
  - `aws-us-east-2`
  - `aws-us-west-2`

### North America - Oregon (`us-west1`)

- **Cloud API Code**: `gcp-us-west1`
- **Regional Endpoint**: `us-west1.gcp.api.temporal.io:7233`
- **Private Service Connect Service Attachment URI**: `projects/prod-rbe76zxxzydz4cbdz2xt5b59q/regions/us-west1/serviceAttachments/pl-94w0x`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `gcp-us-central1`
  - `gcp-us-east4`
- **Multi-Cloud Replication**:
  - `aws-ca-central-1`
  - `aws-us-east-1`
  - `aws-us-east-2`
  - `aws-us-west-2`

### North America - Northern Virginia (`us-east4`)

- **Cloud API Code**: `gcp-us-east4`
- **Regional Endpoint**: `us-east4.gcp.api.temporal.io:7233`
- **Private Service Connect Service Attachment URI**: `projects/prod-y399cvr9c2b43es2w3q3e4gvw/regions/us-east4/serviceAttachments/pl-8awsy`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - `gcp-us-central1`
  - `gcp-us-west1`
- **Multi-Cloud Replication**:
  - `aws-ca-central-1`
  - `aws-us-east-1`
  - `aws-us-east-2`
  - `aws-us-west-2`

### Europe - Frankfurt (`europe-west3`)

- **Cloud API Code**: `gcp-europe-west3`
- **Regional Endpoint**: `europe-west3.gcp.api.temporal.io:7233`
- **Private Service Connect Service Attachment URI**: `projects/prod-kwy7d4faxp6qgrgd9x94du36g/regions/europe-west3/serviceAttachments/pl-acgsh`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - None
- **Multi-Cloud Replication**:
  - `aws-eu-central-1`
  - `aws-eu-west-1`
  - `aws-eu-west-2`

### Asia Pacific - Mumbai (`asia-south1`)

- **Cloud API Code**: `gcp-asia-south1`
- **Regional Endpoint**: `asia-south1.gcp.api.temporal.io:7233`
- **Private Service Connect Service Attachment URI**: `projects/prod-d5spc2sfeshws33bg33vwdef7/regions/asia-south1/serviceAttachments/pl-7w7tw`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - None
- **Multi-Cloud Replication**:
  - `aws-ap-northeast-1`
  - `aws-ap-northeast-2`
  - `aws-ap-south-1`
  - `aws-ap-south-2`
  - `aws-ap-southeast-1`
  - `aws-ap-southeast-2`

### Asia Pacific - Jakarta (`asia-southeast2`)

- **Cloud API Code**: `gcp-asia-southeast2`
- **Regional Endpoint**: `gcp-asia-southeast2.region.tmprl.cloud`
- **Private Service Connect Service Attachment URI**: `projects/prod-bsbyrfwqqq885qkcr3s43y524/regions/asia-southeast2/serviceAttachments/pl-c3ayi`
- **Same Region Replication**:  Not Available
- **Multi-Region Replication**:
  - None
- **Multi-Cloud Replication**:
  - None
