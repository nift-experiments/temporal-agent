# Data encryption

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Payload Codecs encrypt Workflow inputs, outputs, and Signals before they reach the Temporal Service, so plaintext stays on hosts you control.

The Temporal Service persists what your Workflows send it.
Workflow inputs and results, Activity results, Signal and Query payloads, and memos are all recorded in the [Event History](/workflow-execution/event#event-history) and stay there for the length of the Namespace [Retention Period](/temporal-service/temporal-server#retention-period).

A [Payload Codec](/payload-codec) encrypts those Payloads before they leave your process.
The Service stores ciphertext, and the data exists unencrypted only on the Clients and Workers you run, on hosts you control.
Temporal ships no default codec: the default [Data Converter](/dataconversion) serializes to JSON without encrypting, so encryption is something you add.

Encrypted Payloads are unreadable in the Web UI and CLI, which is what a [Codec Server](/codec-server) is for.
It's an HTTP server you run that holds the same decode logic as your codec.
The Web UI and CLI send Payloads to it and display what it returns, so decrypted values reach the browser and the terminal only. The copy on the Temporal Service stays encrypted.

## What you operate

Encryption is opt-in, and each piece of it is yours to run:

- **The codec.** You choose the cipher and write the `encode` and `decode` logic. Temporal doesn't hold or generate your keys.
- **Key distribution.** Your Workers and your Codec Server need the same keys, which usually means [key management](/key-management) infrastructure you already have or have to stand up.
- **The Codec Server.** You host it, secure it, and control access to it. Because it decodes sensitive data through a single API call, restrict it by putting it behind a VPN or adding authentication if it's reachable from the internet. It also needs [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) enabled to answer the Web UI.

Where the endpoint gets configured depends on where the Temporal Service runs:

- **Temporal Cloud.** A [Namespace Admin](/cloud/manage-access/roles-and-permissions#namespace-level-permissions) sets the Codec Server endpoint on the Namespace, which enables it for everyone on that Namespace. Cloud can pass a JWT access token with each request so your server can decide, per user, whether to return plaintext.
- **Self-hosted.** The endpoint is set for the whole Temporal Service, though one Codec Server can route per Namespace. You configure Web UI authorization yourself.

Expect the Web UI to send several requests per Workflow Execution, and expect the round trip to add latency when someone views an Event History.

## What a codec doesn't cover

- **Search Attributes** are persisted unencoded so the Visibility store can index them. Anything you need to search on is readable by the Service, so keep sensitive values out of [Search Attributes](/search-attribute) and in encrypted Payloads.
- **Failure messages and stack traces** aren't encoded as codec-capable Payloads by default. Encoding them is an explicit opt-in through the [Failure Converter](/failure-converter).
- **Payloads above the Service size limit** still need [External Storage](/external-storage), whether or not they're encrypted.
- **Nexus Operations** pass through the Data Converter like any other Payload, so caller and handler Workers need compatible converters. See [Nexus security](/nexus/security#payload-encryption-data-converter).

For how converters and codecs work, see the Encyclopedia pages on [data conversion](/dataconversion).
For setting up and securing a Codec Server, see [Codecs and encryption](/production-deployment/data-encryption).

## Resources

- [Data conversion](/dataconversion): How Payloads are serialized, what the default Data Converter does, and where you can substitute your own.
- [Payload Codec](/payload-codec): The encode and decode step that transforms Payloads for encryption or compression.
- [Codec Server](/codec-server): What a Codec Server is, how the Web UI and CLI use it, and how it works with External Storage.
- [Codecs and encryption](/production-deployment/data-encryption): API contract, CORS, authorization, and endpoint setup for running a Codec Server in production.

Or jump straight to the SDK feature guide for implementation details:

- [.NET SDK](/develop/dotnet/best-practices/data-handling/data-encryption): Implement a Payload Codec and attach it to the Client's Data Converter in C# and .NET.
- [Go SDK](/develop/go/data-handling/data-encryption): Implement a Payload Codec and attach it to the Client's Data Converter in Go.
- [Java SDK](/develop/java/best-practices/data-handling/data-encryption): Implement a Payload Codec and attach it to the Client's Data Converter in Java and other JVM languages.
- [Python SDK](/develop/python/data-handling/data-encryption): Implement a Payload Codec and attach it to the Client's Data Converter in Python.
- [Ruby SDK](/develop/ruby/best-practices/data-handling/data-encryption): Implement a Payload Codec and attach it to the Client's Data Converter in Ruby.
- [TypeScript SDK](/develop/typescript/best-practices/data-handling/data-encryption): Implement a Payload Codec and attach it to the Client's Data Converter in TypeScript and JavaScript.
