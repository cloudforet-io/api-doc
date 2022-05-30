---
description:  
---
# Controller

>  **Package : spaceone.api.spot_automation.v1**

## Controller

{% hint style="info" %}
**Controller Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](controller.md#create)|   [CreateControllerRequest](controller.md#createcontrollerrequest) |   [ControllerInfo](controller.md#controllerinfo) |  |
| [**update**](controller.md#update)|   [UpdateControllerRequest](controller.md#updatecontrollerrequest) |   [ControllerInfo](controller.md#controllerinfo) |  |
| [**delete**](controller.md#delete)|   [ControllerRequest](controller.md#controllerrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](controller.md#get)|   [GetControllerRequest](controller.md#getcontrollerrequest) |   [ControllerInfo](controller.md#controllerinfo) |  |
| [**list**](controller.md#list)|   [ControllerQuery](controller.md#controllerquery) |   [ControllersInfo](controller.md#controllersinfo) |  |
| [**stat**](controller.md#stat)|   [ControllerStatQuery](controller.md#controllerstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| [**control**](controller.md#control)|   [ControlRequest](controller.md#controlrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**update_plugin**](controller.md#update_plugin)|   [UpdatePluginRequest](controller.md#updatepluginrequest) |   [ControllerInfo](controller.md#controllerinfo) |  |
| [**verify_plugin**](controller.md#verify_plugin)|   [VerifyPluginRequest](controller.md#verifypluginrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](controller.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateControllerRequest](controller.md#createcontrollerrequest)  </div> | <div style="width:200px; text-align:center;">   [ControllerInfo](controller.md#controllerinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](controller.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateControllerRequest](controller.md#updatecontrollerrequest)  </div> | <div style="width:200px; text-align:center;">   [ControllerInfo](controller.md#controllerinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](controller.md#delete) </div> | <div style="width:200px; text-align:center;">    [ControllerRequest](controller.md#controllerrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](controller.md#get) </div> | <div style="width:200px; text-align:center;">    [GetControllerRequest](controller.md#getcontrollerrequest)  </div> | <div style="width:200px; text-align:center;">   [ControllerInfo](controller.md#controllerinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](controller.md#list) </div> | <div style="width:200px; text-align:center;">    [ControllerQuery](controller.md#controllerquery)  </div> | <div style="width:200px; text-align:center;">   [ControllersInfo](controller.md#controllersinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](controller.md#stat) </div> | <div style="width:200px; text-align:center;">    [ControllerStatQuery](controller.md#controllerstatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**control**](controller.md#control) </div> | <div style="width:200px; text-align:center;">    [ControlRequest](controller.md#controlrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update_plugin**](controller.md#update_plugin) </div> | <div style="width:200px; text-align:center;">    [UpdatePluginRequest](controller.md#updatepluginrequest)  </div> | <div style="width:200px; text-align:center;">   [ControllerInfo](controller.md#controllerinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**verify_plugin**](controller.md#verify_plugin) </div> | <div style="width:200px; text-align:center;">    [VerifyPluginRequest](controller.md#verifypluginrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> | 
 

 
### create
> **POST** /spot-automation/v1/controllers
>


| Type | Message |
| :--- | :--- |
| Request | [CreateControllerRequest](controller.md#createcontrollerrequest) |
| Response |  [ControllerInfo](controller.md#controllerinfo)  |
 
 

 
### update
> **PUT** /spot-automation/v1/controller/{controller_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateControllerRequest](controller.md#updatecontrollerrequest) |
| Response |  [ControllerInfo](controller.md#controllerinfo)  |
 
 

 
### delete
> **DELETE** /spot-automation/v1/controller/{controller_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ControllerRequest](controller.md#controllerrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /spot-automation/v1/controller/{controller_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetControllerRequest](controller.md#getcontrollerrequest) |
| Response |  [ControllerInfo](controller.md#controllerinfo)  |
 
 

 
### list
> **GET** /spot-automation/v1/controllers
>
> **POST** /spot-automation/v1/controllers/search



| Type | Message |
| :--- | :--- |
| Request | [ControllerQuery](controller.md#controllerquery) |
| Response |  [ControllersInfo](controller.md#controllersinfo)  |
 
 

 
### stat
> **POST** /spot-automation/v1/controllers/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ControllerStatQuery](controller.md#controllerstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |
 
 

 
### control
> **POST** /spot-automation/v1/controller/{controller_id}/control
>


| Type | Message |
| :--- | :--- |
| Request | [ControlRequest](controller.md#controlrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### update_plugin
> **PUT** /spot-automation/v1/controller/{controller_id}/plugin
>


| Type | Message |
| :--- | :--- |
| Request | [UpdatePluginRequest](controller.md#updatepluginrequest) |
| Response |  [ControllerInfo](controller.md#controllerinfo)  |
 
 

 
### verify_plugin
> **POST** /spot-automation/v1/controller/{controller_id}/plugin/verify
>


| Type | Message |
| :--- | :--- |
| Request | [VerifyPluginRequest](controller.md#verifypluginrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |


## 

## Message

### ControlRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| controller_id |string|✅| |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| secret_id |string|❌| |
| domain_id |string|✅| |
| use_cache |bool|❌| |

### ControllerInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| controller_id |string | |
| name |string | |
| provider |string | |
| capability |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| plugin_info |[PluginInfo](controller.md#plugininfo) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| created_at |string | |
| domain_id |string | |

### ControllerQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| controller_id |string|❌| |
| name |string|❌| |
| domain_id |string|✅| |

### ControllerRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| controller_id |string|✅| |
| domain_id |string|✅| |

### ControllerStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### ControllersInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ControllerInfo](controller.md#controllerinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateControllerRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| plugin_info |[PluginInfo](controller.md#plugininfo)|✅| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### GetControllerRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| controller_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### PluginInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| plugin_id |string | |
| version |string | |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| provider |string | |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### UpdateControllerRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| controller_id |string|✅| |
| name |string|❌| |
| plugin_info |[PluginInfo](controller.md#plugininfo)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### UpdatePluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| controller_id |string|✅| |
| version |string|❌| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### VerifyPluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| controller_id |string|✅| |
| secret_id |string|❌| |
| domain_id |string|✅| |
