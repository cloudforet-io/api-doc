---
description: null
---

# Handler

> **Package : spaceone.api.core.v1**

## Message

### AuthenticationRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain\_id | string |  |  |

### AuthenticationResponse

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain\_id | string |  |  |
| 2 | public\_key | string |  |  |

### AuthorizationRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | service | string |  |  |
| 2 | api\_class | string |  |  |
| 3 | method | string |  |  |
| 4 | parameter | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |

### AuthorizationResponse

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | role\_type | string |  |  |
| 2 | changed\_parameter | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |

### EventRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | service | string |  |  |
| 2 | api\_class | string |  |  |
| 3 | method | string |  |  |
| 4 | event\_type | string |  |  |
| 5 | message | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |

