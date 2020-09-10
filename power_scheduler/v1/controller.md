---
description:  
---
# Controller

>  **Package : spaceone.api.power_scheduler.v1**

## Controller

{% hint style="info" %}
**Controller Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](controller.md#create)|   [CreateControllerRequest](controller.md#createcontrollerrequest) |   [ControllerInfo](controller.md#controllerinfo) |  |
| 2 | [**update**](controller.md#update)|   [UpdateControllerRequest](controller.md#updatecontrollerrequest) |   [ControllerInfo](controller.md#controllerinfo) |  |
| 3 | [**delete**](controller.md#delete)|   [ControllerRequest](controller.md#controllerrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](controller.md#get)|   [GetControllerRequest](controller.md#getcontrollerrequest) |   [ControllerInfo](controller.md#controllerinfo) |  |
| 5 | [**list**](controller.md#list)|   [ControllerQuery](controller.md#controllerquery) |   [ControllersInfo](controller.md#controllersinfo) |  |
| 6 | [**stat**](controller.md#stat)|   [ControllerStatQuery](controller.md#controllerstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /power-scheduler/v1/controllers
>


| Type | Message |
| :--- | :--- |
| Request | [CreateControllerRequest](controller.md#createcontrollerrequest) |
| Response |  [ControllerInfo](controller.md#controllerinfo)  |
 
 

 
### update
> **PUT** /power-scheduler/v1/controller/{controller_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateControllerRequest](controller.md#updatecontrollerrequest) |
| Response |  [ControllerInfo](controller.md#controllerinfo)  |
 
 

 
### delete
> **DELETE** /power-scheduler/v1/controller/{controller_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ControllerRequest](controller.md#controllerrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /power-scheduler/v1/controller/{controller_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetControllerRequest](controller.md#getcontrollerrequest) |
| Response |  [ControllerInfo](controller.md#controllerinfo)  |
 
 

 
### list
> **GET** /power-scheduler/v1/controllers
>
> **POST** /power-scheduler/v1/controllers/search



| Type | Message |
| :--- | :--- |
| Request | [ControllerQuery](controller.md#controllerquery) |
| Response |  [ControllersInfo](controller.md#controllersinfo)  |
 
 

 
### stat
> **POST** /power-scheduler/v1/controllers/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ControllerStatQuery](controller.md#controllerstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### ControllerInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | controller_id |string | |
| 2 | name |string | |
| 3 | provider |string | |
| 4 | capability |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 5 | plugin_info |[PluginInfo](controller.md#plugininfo) | |
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 7 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |
| 8 | domain_id |string | |

### ControllerQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | controller_id |string|❌| |
| 3 | name |string|❌| |
| 4 | domain_id |string|✅| |

### ControllerRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | controller_id |string|✅| |
| 2 | domain_id |string|✅| |

### ControllerStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### ControllersInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[ControllerInfo](controller.md#controllerinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateControllerRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | plugin_info |[PluginInfo](controller.md#plugininfo)|✅| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | domain_id |string|✅| |

### GetControllerRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | controller_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### PluginInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | plugin_id |string | |
| 2 | version |string | |
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 4 | provider |string | |
| 5 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### UpdateControllerRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | controller_id |string|✅| |
| 2 | name |string|❌| |
| 3 | plugin_info |[PluginInfo](controller.md#plugininfo)|❌| |
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 5 | domain_id |string|✅| |
