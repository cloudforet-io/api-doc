---
description:  
---
# Device type

>  **Package : spaceone.api.inventory.v1**

## DeviceType

{% hint style="info" %}
**DeviceType Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](device-type.md#create)|   [CreateDeviceTypeRequest](device-type.md#createdevicetyperequest) |   [DeviceTypeInfo](device-type.md#devicetypeinfo) |  |
| 2 | [**update**](device-type.md#update)|   [UpdateDeviceTypeRequest](device-type.md#updatedevicetyperequest) |   [DeviceTypeInfo](device-type.md#devicetypeinfo) |  |
| 3 | [**delete**](device-type.md#delete)|   [DeviceTypeRequest](device-type.md#devicetyperequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](device-type.md#get)|   [GetDeviceTypeRequest](device-type.md#getdevicetyperequest) |   [DeviceTypeInfo](device-type.md#devicetypeinfo) |  |
| 5 | [**list**](device-type.md#list)|   [DeviceTypeQuery](device-type.md#devicetypequery) |   [DeviceTypesInfo](device-type.md#devicetypesinfo) |  |
| 6 | [**stat**](device-type.md#stat)|   [DeviceTypeStatQuery](device-type.md#devicetypestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /inventory/v1/device-types
>


| Type | Message |
| :--- | :--- |
| Request | [CreateDeviceTypeRequest](device-type.md#createdevicetyperequest) |
| Response |  [DeviceTypeInfo](device-type.md#devicetypeinfo)  |
 
 

 
### update
> **PUT** /inventory/v1/device-type/{device_type_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateDeviceTypeRequest](device-type.md#updatedevicetyperequest) |
| Response |  [DeviceTypeInfo](device-type.md#devicetypeinfo)  |
 
 

 
### delete
> **DELETE** /inventory/v1/device-type/{device_type_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DeviceTypeRequest](device-type.md#devicetyperequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /inventory/v1/device-type/{device_type_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetDeviceTypeRequest](device-type.md#getdevicetyperequest) |
| Response |  [DeviceTypeInfo](device-type.md#devicetypeinfo)  |
 
 

 
### list
> **GET** /inventory/v1/device-types
>
> **POST** /inventory/v1/device-types/search



| Type | Message |
| :--- | :--- |
| Request | [DeviceTypeQuery](device-type.md#devicetypequery) |
| Response |  [DeviceTypesInfo](device-type.md#devicetypesinfo)  |
 
 

 
### stat
> **POST** /inventory/v1/device-types/stat
>


| Type | Message |
| :--- | :--- |
| Request | [DeviceTypeStatQuery](device-type.md#devicetypestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateDeviceTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | parent_device_type_id |string|❌| |
| 3 | labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| 4 | template |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 5 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 6 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 7 | domain_id |string|✅| |

### DeviceTypeInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | device_type_id |string | |
| 2 | name |string | |
| 3 | labels |list of string | |
| 4 | parent_device_type_info |[DeviceTypeInfo](device-type.md#devicetypeinfo) | |
| 5 | template |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 6 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 7 | tags |list of spaceone.api.core.v1.Tag | |
| 8 | domain_id |string | |
| 9 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |
| 10 | updated_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |

### DeviceTypeQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | device_type_id |string|❌| |
| 3 | name |string|❌| |
| 4 | domain_id |string|❌| |

### DeviceTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | device_type_id |string|✅| |
| 2 | domain_id |string|✅| |

### DeviceTypeStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### DeviceTypesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of DeviceTypeInfo](device-type.md#devicetypeinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetDeviceTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | device_type_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### UpdateDeviceTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | device_type_id |string|✅| |
| 2 | force |bool|❌| |
| 3 | labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| 4 | template |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 5 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 6 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 7 | domain_id |string|✅| |
