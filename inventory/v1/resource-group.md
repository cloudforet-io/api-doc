---
description:  
---
# Resource group

>  **Package : spaceone.api.inventory.v1**

## ResourceGroup

{% hint style="info" %}
**ResourceGroup Methods:**

{%  endhint %}


| Method | Request | Response |
| :-----: | :--------: | :--------: |
| [**create**](resource-group.md#create)|   [CreateResourceGroupRequest](resource-group.md#createresourcegrouprequest) |   [ResourceGroupInfo](resource-group.md#resourcegroupinfo) |
| [**update**](resource-group.md#update)|   [UpdateResourceGroupRequest](resource-group.md#updateresourcegrouprequest) |   [ResourceGroupInfo](resource-group.md#resourcegroupinfo) |
| [**delete**](resource-group.md#delete)|   [ResourceGroupRequest](resource-group.md#resourcegrouprequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](resource-group.md#get)|   [GetResourceGroupRequest](resource-group.md#getresourcegrouprequest) |   [ResourceGroupInfo](resource-group.md#resourcegroupinfo) |
| [**list**](resource-group.md#list)|   [ResourceGroupQuery](resource-group.md#resourcegroupquery) |   [ResourceGroupsInfo](resource-group.md#resourcegroupsinfo) |
| [**stat**](resource-group.md#stat)|   [ResourceGroupStatQuery](resource-group.md#resourcegroupstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
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
