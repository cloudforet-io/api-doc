---
description:  
---
# Handler

>  **Package : spaceone.api.core.v1**

## Message

### AuthenticationRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string | ||

### AuthenticationResponse
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string | ||
| 2 | public_key |string | ||

### AuthorizationRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | service |string | ||
| 2 | api_class |string | ||
| 3 | method |string | ||
| 4 | parameter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||

### AuthorizationResponse
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | role_type |string | ||
| 2 | changed_parameter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||

### EventRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | service |string | ||
| 2 | api_class |string | ||
| 3 | method |string | ||
| 4 | event_type |string | ||
| 5 | message |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
