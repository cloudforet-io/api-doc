---
description:  
---
# Role

>  **Package : spaceone.api.identity.v1**

## Role

{% hint style="info" %}
**Role Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :--- | :--- | :--- | :--- |
| [**create**](role.md#create)|   [CreateRoleRequest](role.md#createrolerequest) |   [RoleInfo](role.md#roleinfo) |  |
| [**update**](role.md#update)|   [UpdateRoleRequest](role.md#updaterolerequest) |   [RoleInfo](role.md#roleinfo) |  |
| [**delete**](role.md#delete)|   [RoleRequest](role.md#rolerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](role.md#get)|   [GetRoleRequest](role.md#getrolerequest) |   [RoleInfo](role.md#roleinfo) |  |
| [**list**](role.md#list)|   [RoleQuery](role.md#rolequery) |   [RolesInfo](role.md#rolesinfo) |  |
| [**stat**](role.md#stat)|   [RoleStatQuery](role.md#rolestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /identity/v1/roles
>


| Type | Message |
| :--- | :--- |
| Request | [CreateRoleRequest](role.md#createrolerequest) |
| Response |  [RoleInfo](role.md#roleinfo)  |
 
 

 
### update
> **PUT** /identity/v1/roles/{role_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateRoleRequest](role.md#updaterolerequest) |
| Response |  [RoleInfo](role.md#roleinfo)  |
 
 

 
### delete
> **DELETE** /identity/v1/roles/{role_id}
>


| Type | Message |
| :--- | :--- |
| Request | [RoleRequest](role.md#rolerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /identity/v1/roles/{role_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetRoleRequest](role.md#getrolerequest) |
| Response |  [RoleInfo](role.md#roleinfo)  |
 
 

 
### list
> **GET** /identity/v1/roles
>
> **POST** /identity/v1/roles/search



| Type | Message |
| :--- | :--- |
| Request | [RoleQuery](role.md#rolequery) |
| Response |  [RolesInfo](role.md#rolesinfo)  |
 
 

 
### stat
> **POST** /identity/v1/roles/stat
>


| Type | Message |
| :--- | :--- |
| Request | [RoleStatQuery](role.md#rolestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateRoleRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">role_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>SYSTEM</li>
          	<li>DOMAIN</li>
          	<li>PROJECT</li>
        </ul></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">policies</td>
      <td style="text-align:left"><a href="role.md#rolepolicy">list of RolePolicy</a></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">page_permissions</td>
      <td style="text-align:left"><a href="role.md#pagepermission">list of PagePermission</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### GetRoleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| role_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### PagePermission
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">page</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">permission</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>VIEW</li>
          	<li>MANAGE</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### RoleInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">role_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">role_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>SYSTEM</li>
          	<li>DOMAIN</li>
          	<li>PROJECT</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">policies</td>
      <td style="text-align:left"><a href="role.md#rolepolicy">list of RolePolicy</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">page_permissions</td>
      <td style="text-align:left"><a href="role.md#pagepermission">list of PagePermission</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">deleted_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### RolePolicy
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">policy_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>MANAGED</li>
          	<li>CUSTOM</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">policy_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### RoleQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">role_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">role_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>SYSTEM</li>
          	<li>DOMAIN</li>
          	<li>PROJECT</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">policy_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### RoleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| role_id |string|✅| |
| domain_id |string|✅| |

### RoleStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### RolesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of RoleInfo](role.md#roleinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateRoleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| role_id |string|✅| |
| name |string|❌| |
| policies |[list of RolePolicy](role.md#rolepolicy)|❌| |
| page_permissions |[list of PagePermission](role.md#pagepermission)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| release_page_permissions |bool|❌| |
| domain_id |string|✅| |
