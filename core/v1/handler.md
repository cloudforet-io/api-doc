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
| 2 | resource | string |  |  |
| 3 | verb | string |  |  |
| 4 | project\_id | string |  |  |

### AuthorizationResponse

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | role\_type | string |  |  |
| 2 | allowed | bool |  |  |
| 3 | reason | string |  |  |

### EventRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | service | string |  |  |
| 2 | resource | string |  |  |
| 3 | verb | string |  |  |
| 4 | state | string |  |  |
| 5 | message | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |

