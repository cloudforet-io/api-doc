---
description:  
---
# Role

>  **Package : spaceone.api.identity.v1**

## Role

{% hint style="info" %}
**Role Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Role.md#create)| [CreateRoleRequest](Role.md#createrolerequest) | [RoleInfo](Role.md#roleinfo) |  |
| 2 | [update](Role.md#update)| [UpdateRoleRequest](Role.md#updaterolerequest) | [RoleInfo](Role.md#roleinfo) |  |
| 3 | [delete](Role.md#delete)| [RoleRequest](Role.md#rolerequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [get](Role.md#get)| [GetRoleRequest](Role.md#getrolerequest) | [RoleInfo](Role.md#roleinfo) |  |
| 5 | [list](Role.md#list)| [RoleQuery](Role.md#rolequery) | [RolesInfo](Role.md#rolesinfo) |  |
| 6 | [stat](Role.md#stat)| [RoleStatQuery](Role.md#rolestatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /identity/v1/roles
>



| Type | Message |
| :--- | :--- |
| Request | [CreateRoleRequest](Role.md#createrolerequest) |
| Response |  [RoleInfo](Role.md#roleinfo)  |



### update
> **PUT** /identity/v1/roles/{role_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateRoleRequest](Role.md#updaterolerequest) |
| Response |  [RoleInfo](Role.md#roleinfo)  |



### delete
> **DELETE** /identity/v1/roles/{role_id}
>



| Type | Message |
| :--- | :--- |
| Request | [RoleRequest](Role.md#rolerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /identity/v1/roles/{role_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetRoleRequest](Role.md#getrolerequest) |
| Response |  [RoleInfo](Role.md#roleinfo)  |



### list
> **GET** /identity/v1/roles
>
> **POST** /identity/v1/roles/search




| Type | Message |
| :--- | :--- |
| Request | [RoleQuery](Role.md#rolequery) |
| Response |  [RolesInfo](Role.md#rolesinfo)  |



### stat
> **POST** /identity/v1/roles/stat
>



| Type | Message |
| :--- | :--- |
| Request | [RoleStatQuery](Role.md#rolestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreateRoleRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">✅</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">✅</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">role_type</td>
      <td style="text-align:left">
<p>RoleType</p>
        <ul>
          	<li>NONE</li>
          	<li>SYSTEM</li>
          	<li>DOMAIN</li>
          	<li>PROJECT</li>
        </ul>
</td><td style="text-align:left">✅</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">policies</td>
      <td style="text-align:left">
<a href="Role.md#rolepolicy">RolePolicy</a>
</td><td style="text-align:left">✅</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
  </tbody>
</table>


### GetRoleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | role_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### RoleInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">role_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">role_type</td>
      <td style="text-align:left">
<p>RoleType</p>
        <ul>
          	<li>NONE</li>
          	<li>SYSTEM</li>
          	<li>DOMAIN</li>
          	<li>PROJECT</li>
        </ul>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">policies</td>
      <td style="text-align:left">
<a href="Role.md#rolepolicy">RolePolicy</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">deleted_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
  </tbody>
</table>


### RolePolicy
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">policy_type</td>
      <td style="text-align:left">
<p>RolePolicy.PolicyType</p>
        <ul>
          	<li>NONE</li>
          	<li>MANAGED</li>
          	<li>CUSTOM</li>
        </ul>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">url</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">policy_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
  </tbody>
</table>


### RoleQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left">
<a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a>
</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">role_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">role_type</td>
      <td style="text-align:left">
<p>RoleType</p>
        <ul>
          	<li>NONE</li>
          	<li>SYSTEM</li>
          	<li>DOMAIN</li>
          	<li>PROJECT</li>
        </ul>
</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">✅</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
  </tbody>
</table>


### RoleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | role_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### RoleStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### RolesInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[RoleInfo](Role.md#roleinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### UpdateRoleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | role_id |string |✅ ||
| 2 | name |string |❌ ||
| 3 | domain_id |string |✅ ||
| 4 | policies |[RolePolicy](Role.md#rolepolicy) |✅ ||
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
