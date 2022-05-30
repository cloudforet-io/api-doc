---
description:  
---
# Controller

>  **Package : spaceone.api.power_scheduler.v1**

## Controller

{% hint style="info" %}
**Controller Methods:**

{%  endhint %}


| Method | Request | Response | Description |
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

<table style="border-collapse: collapse; text-align: left; line-height: 1.5;">
    <thead>
    <tr>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Method</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Request</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Response</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">create</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CreateControllerRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ControllerInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdateControllerRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ControllerInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">delete</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ControllerRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   GetControllerRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ControllerInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ControllerQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ControllersInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ControllerStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">control</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ControlRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update_plugin</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdatePluginRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ControllerInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">verify_plugin</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   VerifyPluginRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
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
 
 

 
### control
> **POST** /power-scheduler/v1/controller/{controller_id}/control
>


| Type | Message |
| :--- | :--- |
| Request | [ControlRequest](controller.md#controlrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### update_plugin
> **PUT** /power-scheduler/v1/controller/{controller_id}/plugin
>


| Type | Message |
| :--- | :--- |
| Request | [UpdatePluginRequest](controller.md#updatepluginrequest) |
| Response |  [ControllerInfo](controller.md#controllerinfo)  |
 
 

 
### verify_plugin
> **POST** /power-scheduler/v1/controller/{controller_id}/plugin/verify
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
