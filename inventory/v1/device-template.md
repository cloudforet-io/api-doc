---
description:  
---
# Device template

>  **Package : spaceone.api.inventory.v1**

## DeviceTemplate

{% hint style="info" %}
**DeviceTemplate Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](device-template.md#create)|   [CreateDeviceTemplateRequest](device-template.md#createdevicetemplaterequest) |   [DeviceTemplateInfo](device-template.md#devicetemplateinfo) |  |
| 2 | [**update**](device-template.md#update)|   [UpdateDeviceTemplateRequest](device-template.md#updatedevicetemplaterequest) |   [DeviceTemplateInfo](device-template.md#devicetemplateinfo) |  |
| 3 | [**delete**](device-template.md#delete)|   [DeviceTemplateRequest](device-template.md#devicetemplaterequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](device-template.md#get)|   [GetDeviceTemplateRequest](device-template.md#getdevicetemplaterequest) |   [DeviceTemplateInfo](device-template.md#devicetemplateinfo) |  |
| 5 | [**list**](device-template.md#list)|   [DeviceTemplateQuery](device-template.md#devicetemplatequery) |   [DeviceTemplatesInfo](device-template.md#devicetemplatesinfo) |  |
| 6 | [**stat**](device-template.md#stat)|   [DeviceTemplateStatQuery](device-template.md#devicetemplatestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /inventory/v1/device-templates
>


| Type | Message |
| :--- | :--- |
| Request | [CreateDeviceTemplateRequest](device-template.md#createdevicetemplaterequest) |
| Response |  [DeviceTemplateInfo](device-template.md#devicetemplateinfo)  |
 
 

 
### update
> **PUT** /inventory/v1/device-template/{device_template_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateDeviceTemplateRequest](device-template.md#updatedevicetemplaterequest) |
| Response |  [DeviceTemplateInfo](device-template.md#devicetemplateinfo)  |
 
 

 
### delete
> **DELETE** /inventory/v1/device-template/{device_template_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DeviceTemplateRequest](device-template.md#devicetemplaterequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /inventory/v1/device-template/{device_template_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetDeviceTemplateRequest](device-template.md#getdevicetemplaterequest) |
| Response |  [DeviceTemplateInfo](device-template.md#devicetemplateinfo)  |
 
 

 
### list
> **GET** /inventory/v1/device-templates
>
> **POST** /inventory/v1/device-templates/search



| Type | Message |
| :--- | :--- |
| Request | [DeviceTemplateQuery](device-template.md#devicetemplatequery) |
| Response |  [DeviceTemplatesInfo](device-template.md#devicetemplatesinfo)  |
 
 

 
### stat
> **POST** /inventory/v1/device-templates/stat
>


| Type | Message |
| :--- | :--- |
| Request | [DeviceTemplateStatQuery](device-template.md#devicetemplatestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateDeviceTemplateRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | device_type_id |string|✅| |
| 3 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 4 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 5 | domain_id |string|✅| |

### DeviceTemplateInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | device_template_id |string | |
| 2 | name |string | |
| 3 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 4 | tags |list of spaceone.api.core.v1.Tag | |
| 5 | domain_id |string | |
| 6 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |

### DeviceTemplateQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | device_template_id |string|❌| |
| 3 | name |string|❌| |
| 4 | device_type_id |string|❌| |
| 5 | domain_id |string|❌| |

### DeviceTemplateRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | device_template_id |string|✅| |
| 2 | domain_id |string|✅| |

### DeviceTemplateStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### DeviceTemplatesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of DeviceTemplateInfo](device-template.md#devicetemplateinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetDeviceTemplateRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | device_template_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### UpdateDeviceTemplateRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | device_template_id |string|✅| |
| 2 | name |string|❌| |
| 3 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 5 | domain_id |string|✅| |
