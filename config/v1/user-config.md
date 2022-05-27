---
description: UserConfig API which configure environments for user
---
# User config

>  **Package : spaceone.api.config.v1**

## UserConfig

{% hint style="info" %}
**UserConfig Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :--- | :--- | :--- | :--- |
| [**create**](user-config.md#create)|   [SetUserConfigRequest](user-config.md#setuserconfigrequest) |   [UserConfigInfo](user-config.md#userconfiginfo) |  |
| [**update**](user-config.md#update)|   [SetUserConfigRequest](user-config.md#setuserconfigrequest) |   [UserConfigInfo](user-config.md#userconfiginfo) |  |
| [**set**](user-config.md#set)|   [SetUserConfigRequest](user-config.md#setuserconfigrequest) |   [UserConfigInfo](user-config.md#userconfiginfo) |  |
| [**delete**](user-config.md#delete)|   [UserConfigRequest](user-config.md#userconfigrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](user-config.md#get)|   [GetUserConfigRequest](user-config.md#getuserconfigrequest) |   [UserConfigInfo](user-config.md#userconfiginfo) |  |
| [**list**](user-config.md#list)|   [UserConfigQuery](user-config.md#userconfigquery) |   [UserConfigsInfo](user-config.md#userconfigsinfo) |  |
| [**stat**](user-config.md#stat)|   [UserConfigStatQuery](user-config.md#userconfigstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /config/v1/user-configs
>


| Type | Message |
| :--- | :--- |
| Request | [SetUserConfigRequest](user-config.md#setuserconfigrequest) |
| Response |  [UserConfigInfo](user-config.md#userconfiginfo)  |
 
 

 
### update
> **PUT** /config/v1/user-config/{name}
>


| Type | Message |
| :--- | :--- |
| Request | [SetUserConfigRequest](user-config.md#setuserconfigrequest) |
| Response |  [UserConfigInfo](user-config.md#userconfiginfo)  |
 
 

 
### set
> **POST** /config/v1/user-config/{name}
>


| Type | Message |
| :--- | :--- |
| Request | [SetUserConfigRequest](user-config.md#setuserconfigrequest) |
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

### GetUserConfigRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### SetUserConfigRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### UserConfigInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| name |string | |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| user_id |string | |
| domain_id |string | |
| created_at |string | |
| updated_at |string | |

### UserConfigQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| name |string|❌| |
| user_id |string|❌| |
| domain_id |string|✅| |

### UserConfigRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| domain_id |string|✅| |

### UserConfigStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### UserConfigsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of UserConfigInfo](user-config.md#userconfiginfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
