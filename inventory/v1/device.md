---
description:  
---
# Device

>  **Package : spaceone.api.inventory.v1**

## Device

{% hint style="info" %}
**Device Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](device.md#create)|   [CreateDeviceRequest](device.md#createdevicerequest) |   [DeviceInfo](device.md#deviceinfo) |  |
| 2 | [**update**](device.md#update)|   [UpdateDeviceRequest](device.md#updatedevicerequest) |   [DeviceInfo](device.md#deviceinfo) |  |
| 3 | [**pin_data**](device.md#pin_data)|   [PinDeviceRequest](device.md#pindevicerequest) |   [DeviceInfo](device.md#deviceinfo) |  |
| 4 | [**delete**](device.md#delete)|   [DeviceRequest](device.md#devicerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**get**](device.md#get)|   [GetDeviceRequest](device.md#getdevicerequest) |   [DeviceInfo](device.md#deviceinfo) |  |
| 6 | [**list**](device.md#list)|   [DeviceQuery](device.md#devicequery) |   [DevicesInfo](device.md#devicesinfo) |  |
| 7 | [**stat**](device.md#stat)|   [DeviceStatQuery](device.md#devicestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /inventory/v1/devices
>


| Type | Message |
| :--- | :--- |
| Request | [CreateDeviceRequest](device.md#createdevicerequest) |
| Response |  [DeviceInfo](device.md#deviceinfo)  |
 
 

 
### update
> **PUT** /inventory/v1/device/{device_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateDeviceRequest](device.md#updatedevicerequest) |
| Response |  [DeviceInfo](device.md#deviceinfo)  |
 
 

 
### pin_data
> **PUT** /inventory/v1/device/{device_id}/pin-data
>


| Type | Message |
| :--- | :--- |
| Request | [PinDeviceRequest](device.md#pindevicerequest) |
| Response |  [DeviceInfo](device.md#deviceinfo)  |
 
 

 
### delete
> **DELETE** /inventory/v1/device/{device_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DeviceRequest](device.md#devicerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /inventory/v1/device/{device_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetDeviceRequest](device.md#getdevicerequest) |
| Response |  [DeviceInfo](device.md#deviceinfo)  |
 
 

 
### list
> **GET** /inventory/v1/devices
>
> **POST** /inventory/v1/devices/search



| Type | Message |
| :--- | :--- |
| Request | [DeviceQuery](device.md#devicequery) |
| Response |  [DevicesInfo](device.md#devicesinfo)  |
 
 

 
### stat
> **POST** /inventory/v1/devices/stat
>


| Type | Message |
| :--- | :--- |
| Request | [DeviceStatQuery](device.md#devicestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateDeviceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | device_type_id |string|✅| |
| 2 | project_id |string|❌| |
| 3 | region_code |string|❌| |
| 4 | region_type |string|❌| |
| 5 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 6 | reference |[DeviceReference](device.md#devicereference)|❌| |
| 7 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 8 | domain_id |string|✅| |

### DeviceInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">device_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>STATE_NONE</li>
          	<li>INSTOCK</li>
          	<li>INSERVICE</li>
          	<li>DELETED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">region_code</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">region_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">device_type_info</td>
      <td style="text-align:left"><a href="device.md#devicetypeinfo">DeviceTypeInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">reference</td>
      <td style="text-align:left"><a href="device.md#devicereference">DeviceReference</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left">list of spaceone.api.core.v1.Tag</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">collection_info</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### DeviceQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | device_id |string|❌| |
| 3 | device_type_id |string|❌| |
| 4 | project_id |string|❌| |
| 5 | region_code |string|❌| |
| 6 | region_type |string|❌| |
| 7 | domain_id |string|✅| |

### DeviceReference
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | resource_id |string | |
| 2 | external_link |string | |

### DeviceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | device_id |string|✅| |
| 2 | domain_id |string|✅| |

### DeviceStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### DevicesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of DeviceInfo](device.md#deviceinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetDeviceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | device_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### PinDeviceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | device_id |string|✅| |
| 2 | keys |list of string|✅| |
| 3 | domain_id |string|✅| |

### UpdateDeviceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | device_id |string|✅| |
| 2 | project_id |string|❌| |
| 3 | region_code |string|❌| |
| 4 | region_type |string|❌| |
| 5 | release_project |bool|❌| |
| 6 | release_region |bool|❌| |
| 7 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 8 | reference |[DeviceReference](device.md#devicereference)|❌| |
| 9 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 10 | domain_id |string|✅| |
