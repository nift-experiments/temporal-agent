# Data handling - Java SDK

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

All data sent to and from the Temporal Service passes through the **Data Converter**. The Data Converter has three
layers that handle different concerns:

![The Flow of Data through a Data Converter](/diagrams/data-converter-flow-with-external-storage.svg)

Of these three layers, only the PayloadConverter is required. Temporal uses a default PayloadConverter that handles JSON
serialization. The PayloadCodec and ExternalStorage layers are optional. You only need to customize these layers when
your application requires non-JSON types, encryption, or payload offloading.

|                           | [PayloadConverter](/develop/java/best-practices/data-handling/data-conversion) | [PayloadCodec](/develop/java/best-practices/data-handling/data-encryption) | [External Storage](/develop/java/data-handling/external-storage) |
| ------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------- |
| **Purpose**               | Serialize application data to bytes                               | Transform encoded payloads (encrypt, compress)                | Offload large Payloads to an external store                     |
| **Default**               | JSON serialization                                                | None (passthrough)                                            | Disabled                                                        |

For a deeper conceptual explanation, see the [Data Conversion encyclopedia](/dataconversion) and [External Storage](/external-storage).
