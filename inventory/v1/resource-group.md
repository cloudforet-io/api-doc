---
description:  
---
# Resource group

>  **Package : spaceone.api.inventory.v1**

## ResourceGroup

{% hint style="info" %}
**ResourceGroup Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](resource-group.md#create)|   [CreateResourceGroupRequest](resource-group.md#createresourcegrouprequest) |   [ResourceGroupInfo](resource-group.md#resourcegroupinfo) |  |
| [**update**](resource-group.md#update)|   [UpdateResourceGroupRequest](resource-group.md#updateresourcegrouprequest) |   [ResourceGroupInfo](resource-group.md#resourcegroupinfo) |  |
| [**delete**](resource-group.md#delete)|   [ResourceGroupRequest](resource-group.md#resourcegrouprequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](resource-group.md#get)|   [GetResourceGroupRequest](resource-group.md#getresourcegrouprequest) |   [ResourceGroupInfo](resource-group.md#resourcegroupinfo) |  |
| [**list**](resource-group.md#list)|   [ResourceGroupQuery](resource-group.md#resourcegroupquery) |   [ResourceGroupsInfo](resource-group.md#resourcegroupsinfo) |  |
| [**stat**](resource-group.md#stat)|   [ResourceGroupStatQuery](resource-group.md#resourcegroupstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

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
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CreateResourceGroupRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ResourceGroupInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdateResourceGroupRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ResourceGroupInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">delete</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ResourceGroupRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   GetResourceGroupRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ResourceGroupInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ResourceGroupQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ResourceGroupsInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ResourceGroupStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
### create
> **POST** /inventory/v1/resource-groups
>


| Type | Message |
| :--- | :--- |
| Request | [CreateResourceGroupRequest](resource-group.md#createresourcegrouprequest) |
| Response |  [ResourceGroupInfo](resource-group.md#resourcegroupinfo)  |
 
 

 
### update
> **PUT** /inventory/v1/resource-group/{resource_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateResourceGroupRequest](resource-group.md#updateresourcegrouprequest) |
| Response |  [ResourceGroupInfo](resource-group.md#resourcegroupinfo)  |
 
 

 
### delete
> **DELETE** /inventory/v1/resource-group/{resource_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ResourceGroupRequest](resource-group.md#resourcegrouprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /inventory/v1/resource-group/{resource_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetResourceGroupRequest](resource-group.md#getresourcegrouprequest) |
| Response |  [ResourceGroupInfo](resource-group.md#resourcegroupinfo)  |
 
 

 
### list
> **GET** /inventory/v1/resource-groups
>
> **POST** /inventory/v1/resource-groups/search



| Type | Message |
| :--- | :--- |
| Request | [ResourceGroupQuery](resource-group.md#resourcegroupquery) |
| Response |  [ResourceGroupsInfo](resource-group.md#resourcegroupsinfo)  |
 
 

 
### stat
> **POST** /inventory/v1/resource-groups/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ResourceGroupStatQuery](resource-group.md#resourcegroupstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateResourceGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| resources |[list of Resource](resource-group.md#resource)|✅| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| project_id |string|✅| |
| domain_id |string|✅| |

### GetResourceGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_group_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### Resource
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_type |string|✅| |
| filter |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| keyword |string|❌| |

### ResourceGroupInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_group_id |string | |
| name |string | |
| resources |[list of Resource](resource-group.md#resource) | |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| project_id |string | |
| domain_id |string | |
| created_at |string | |

### ResourceGroupQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| resource_group_id |string|❌| |
| name |string|❌| |
| project_id |string|❌| |
| domain_id |string|✅| |

### ResourceGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_group_id |string|✅| |
| domain_id |string|✅| |

### ResourceGroupStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### ResourceGroupsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ResourceGroupInfo](resource-group.md#resourcegroupinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateResourceGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_group_id |string|✅| |
| name |string|❌| |
| resources |[list of Resource](resource-group.md#resource)|❌| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| release_project |bool|❌| |
| project_id |string|❌| |
| domain_id |string|✅| |
