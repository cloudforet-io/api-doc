---
description:  
---
# Secret group

>  **Package : spaceone.api.secret.v1**

## SecretGroup

{% hint style="info" %}
**SecretGroup Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Secret-group.md#create)| [CreateSecretGroupRequest](Secret-group.md#createsecretgrouprequest) | [SecretGroupInfo](Secret-group.md#secretgroupinfo) |  |
| 2 | [update](Secret-group.md#update)| [UpdateSecretGroupRequest](Secret-group.md#updatesecretgrouprequest) | [SecretGroupInfo](Secret-group.md#secretgroupinfo) |  |
| 3 | [add_secret](Secret-group.md#add_secret)| [SecretGroupSecretRequest](Secret-group.md#secretgroupsecretrequest) | [SecretGroupSecretInfo](Secret-group.md#secretgroupsecretinfo) |  |
| 4 | [remove_secret](Secret-group.md#remove_secret)| [SecretGroupSecretRequest](Secret-group.md#secretgroupsecretrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [delete](Secret-group.md#delete)| [SecretGroupRequest](Secret-group.md#secretgrouprequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 6 | [get](Secret-group.md#get)| [GetSecretGroupRequest](Secret-group.md#getsecretgrouprequest) | [SecretGroupInfo](Secret-group.md#secretgroupinfo) |  |
| 7 | [list](Secret-group.md#list)| [SecretGroupQuery](Secret-group.md#secretgroupquery) | [SecretGroupsInfo](Secret-group.md#secretgroupsinfo) |  |
| 8 | [stat](Secret-group.md#stat)| [SecretGroupStatQuery](Secret-group.md#secretgroupstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /secret/v1/secret-groups
>



| Type | Message |
| :--- | :--- |
| Request | [CreateSecretGroupRequest](Secret-group.md#createsecretgrouprequest) |
| Response |  [SecretGroupInfo](Secret-group.md#secretgroupinfo)  |



### update
> **PUT** /secret/v1/secret-group/{secret_group_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateSecretGroupRequest](Secret-group.md#updatesecretgrouprequest) |
| Response |  [SecretGroupInfo](Secret-group.md#secretgroupinfo)  |



### add_secret
> **POST** /secret/v1/secret-group/{secret_group_id}/secrets
>



| Type | Message |
| :--- | :--- |
| Request | [SecretGroupSecretRequest](Secret-group.md#secretgroupsecretrequest) |
| Response |  [SecretGroupSecretInfo](Secret-group.md#secretgroupsecretinfo)  |



### remove_secret
> **DELETE** /secret/v1/secret-group/{secret_group_id}/secret/{secret_id}
>



| Type | Message |
| :--- | :--- |
| Request | [SecretGroupSecretRequest](Secret-group.md#secretgroupsecretrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### delete
> **DELETE** /secret/v1/secret-group/{secret_group_id}
>



| Type | Message |
| :--- | :--- |
| Request | [SecretGroupRequest](Secret-group.md#secretgrouprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /secret/v1/secret-group/{secret_group_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetSecretGroupRequest](Secret-group.md#getsecretgrouprequest) |
| Response |  [SecretGroupInfo](Secret-group.md#secretgroupinfo)  |



### list
> **GET** /secret/v1/secret-groups
>
> **POST** /secret/v1/secret-groups/search




| Type | Message |
| :--- | :--- |
| Request | [SecretGroupQuery](Secret-group.md#secretgroupquery) |
| Response |  [SecretGroupsInfo](Secret-group.md#secretgroupsinfo)  |



### stat
> **POST** /secret/v1/secret-groups/stat
>



| Type | Message |
| :--- | :--- |
| Request | [SecretGroupStatQuery](Secret-group.md#secretgroupstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreateSecretGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 3 | domain_id |string |✅ ||

### GetSecretGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret_group_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### SecretGroupInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret_group_id |string | ||
| 2 | name |string | ||
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 4 | domain_id |string | ||
| 5 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### SecretGroupQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | secret_group_id |string |❌ ||
| 3 | name |string |❌ ||
| 4 | secret_id |string |❌ ||
| 5 | domain_id |string |✅ ||

### SecretGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret_group_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### SecretGroupSecretInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret_group_info |[SecretGroupInfo](Secret-group.md#secretgroupinfo) | ||
| 2 | secret_info |[SecretInfo](Secret-group.md#secretinfo) | ||
| 3 | domain_id |string | ||

### SecretGroupSecretRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret_group_id |string |✅ ||
| 2 | secret_id |string |✅ ||
| 3 | domain_id |string |✅ ||

### SecretGroupStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### SecretGroupsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[SecretGroupInfo](Secret-group.md#secretgroupinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### UpdateSecretGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret_group_id |string |✅ ||
| 2 | name |string |❌ ||
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | domain_id |string |✅ ||
