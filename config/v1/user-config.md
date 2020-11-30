---
description: Config Map API which configure environments for user
---
# User config

>  **Package : spaceone.api.config.v1**

## UserConfig

{% hint style="info" %}
**UserConfig Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](user-config.md#create)|   [CreateUserConfigRequest](user-config.md#createuserconfigrequest) |   [UserConfigInfo](user-config.md#userconfiginfo) |  |
| 2 | [**update**](user-config.md#update)|   [UpdateUserConfigRequest](user-config.md#updateuserconfigrequest) |   [UserConfigInfo](user-config.md#userconfiginfo) |  |
| 3 | [**delete**](user-config.md#delete)|   [UserConfigRequest](user-config.md#userconfigrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](user-config.md#get)|   [GetUserConfigRequest](user-config.md#getuserconfigrequest) |   [UserConfigInfo](user-config.md#userconfiginfo) |  |
| 5 | [**list**](user-config.md#list)|   [UserConfigQuery](user-config.md#userconfigquery) |   [UserConfigsInfo](user-config.md#userconfigsinfo) |  |
| 6 | [**stat**](user-config.md#stat)|   [UserConfigStatQuery](user-config.md#userconfigstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /config/v1/user-configs
>


| Type | Message |
| :--- | :--- |
| Request | [CreateUserConfigRequest](user-config.md#createuserconfigrequest) |
| Response |  [UserConfigInfo](user-config.md#userconfiginfo)  |
 
 

 
### update
> **PUT** /config/v1/user-config/{name}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateUserConfigRequest](user-config.md#updateuserconfigrequest) |
| Response |  [UserConfigInfo](user-config.md#userconfiginfo)  |
 
 

 
### delete
> **DELETE** /config/v1/user-config/{name}
>


| Type | Message |
| :--- | :--- |
| Request | [UserConfigRequest](user-config.md#userconfigrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /config/v1/user-config/{name}
>


| Type | Message |
| :--- | :--- |
| Request | [GetUserConfigRequest](user-config.md#getuserconfigrequest) |
| Response |  [UserConfigInfo](user-config.md#userconfiginfo)  |
 
 

 
### list
> **GET** /config/v1/user-configs
>
> **POST** /config/v1/user-configs/search



| Type | Message |
| :--- | :--- |
| Request | [UserConfigQuery](user-config.md#userconfigquery) |
| Response |  [UserConfigsInfo](user-config.md#userconfigsinfo)  |
 
 

 
### stat
> **POST** /config/v1/user-configs/stat
>


| Type | Message |
| :--- | :--- |
| Request | [UserConfigStatQuery](user-config.md#userconfigstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateUserConfigRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 3 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 4 | domain_id |string|✅| |

### GetUserConfigRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### UpdateUserConfigRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 3 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 4 | domain_id |string|✅| |

### UserConfigInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | name |string | |
| 2 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 3 | tags |list of spaceone.api.core.v1.Tag | |
| 4 | domain_id |string | |
| 5 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |

### UserConfigQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | name |string|❌| |
| 3 | domain_id |string|✅| |

### UserConfigRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | domain_id |string|✅| |

### UserConfigStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### UserConfigsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of UserConfigInfo](user-config.md#userconfiginfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
