---
description:  
---
# Secret group

>  **Package : spaceone.api.secret.v1**

## SecretGroup

{% hint style="info" %}
**SecretGroup Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](secret-group.md#create)|   [CreateSecretGroupRequest](secret-group.md#createsecretgrouprequest) |   [SecretGroupInfo](secret-group.md#secretgroupinfo) |  |
| [**update**](secret-group.md#update)|   [UpdateSecretGroupRequest](secret-group.md#updatesecretgrouprequest) |   [SecretGroupInfo](secret-group.md#secretgroupinfo) |  |
| [**add_secret**](secret-group.md#add_secret)|   [SecretGroupSecretRequest](secret-group.md#secretgroupsecretrequest) |   [SecretGroupSecretInfo](secret-group.md#secretgroupsecretinfo) |  |
| [**remove_secret**](secret-group.md#remove_secret)|   [SecretGroupSecretRequest](secret-group.md#secretgroupsecretrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**delete**](secret-group.md#delete)|   [SecretGroupRequest](secret-group.md#secretgrouprequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](secret-group.md#get)|   [GetSecretGroupRequest](secret-group.md#getsecretgrouprequest) |   [SecretGroupInfo](secret-group.md#secretgroupinfo) |  |
| [**list**](secret-group.md#list)|   [SecretGroupQuery](secret-group.md#secretgroupquery) |   [SecretGroupsInfo](secret-group.md#secretgroupsinfo) |  |
| [**stat**](secret-group.md#stat)|   [SecretGroupStatQuery](secret-group.md#secretgroupstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

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
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CreateSecretGroupRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   SecretGroupInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdateSecretGroupRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   SecretGroupInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">add_secret</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   SecretGroupSecretRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   SecretGroupSecretInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">remove_secret</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   SecretGroupSecretRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">delete</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   SecretGroupRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   GetSecretGroupRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   SecretGroupInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   SecretGroupQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   SecretGroupsInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   SecretGroupStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
### create
> **POST** /secret/v1/secret-groups
>


| Type | Message |
| :--- | :--- |
| Request | [CreateSecretGroupRequest](secret-group.md#createsecretgrouprequest) |
| Response |  [SecretGroupInfo](secret-group.md#secretgroupinfo)  |
 
 

 
### update
> **PUT** /secret/v1/secret-group/{secret_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateSecretGroupRequest](secret-group.md#updatesecretgrouprequest) |
| Response |  [SecretGroupInfo](secret-group.md#secretgroupinfo)  |
 
 

 
### add_secret
> **POST** /secret/v1/secret-group/{secret_group_id}/secrets
>


| Type | Message |
| :--- | :--- |
| Request | [SecretGroupSecretRequest](secret-group.md#secretgroupsecretrequest) |
| Response |  [SecretGroupSecretInfo](secret-group.md#secretgroupsecretinfo)  |
 
 

 
### remove_secret
> **DELETE** /secret/v1/secret-group/{secret_group_id}/secret/{secret_id}
>


| Type | Message |
| :--- | :--- |
| Request | [SecretGroupSecretRequest](secret-group.md#secretgroupsecretrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### delete
> **DELETE** /secret/v1/secret-group/{secret_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [SecretGroupRequest](secret-group.md#secretgrouprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /secret/v1/secret-group/{secret_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetSecretGroupRequest](secret-group.md#getsecretgrouprequest) |
| Response |  [SecretGroupInfo](secret-group.md#secretgroupinfo)  |
 
 

 
### list
> **GET** /secret/v1/secret-groups
>
> **POST** /secret/v1/secret-groups/search



| Type | Message |
| :--- | :--- |
| Request | [SecretGroupQuery](secret-group.md#secretgroupquery) |
| Response |  [SecretGroupsInfo](secret-group.md#secretgroupsinfo)  |
 
 

 
### stat
> **POST** /secret/v1/secret-groups/stat
>


| Type | Message |
| :--- | :--- |
| Request | [SecretGroupStatQuery](secret-group.md#secretgroupstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateSecretGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### GetSecretGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_group_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### SecretGroupInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| secret_group_id |string | |
| name |string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
| created_at |string | |

### SecretGroupQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| secret_group_id |string|❌| |
| name |string|❌| |
| secret_id |string|❌| |
| domain_id |string|✅| |

### SecretGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_group_id |string|✅| |
| domain_id |string|✅| |

### SecretGroupSecretInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| secret_group_info |[SecretGroupInfo](secret-group.md#secretgroupinfo) | |
| secret_info |[SecretInfo](secret-group.md#secretinfo) | |
| domain_id |string | |

### SecretGroupSecretRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_group_id |string|✅| |
| secret_id |string|✅| |
| domain_id |string|✅| |

### SecretGroupStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### SecretGroupsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of SecretGroupInfo](secret-group.md#secretgroupinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateSecretGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_group_id |string|✅| |
| name |string|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
