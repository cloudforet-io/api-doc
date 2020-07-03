---
description: null
---

# User

> **Package : spaceone.api.identity.v1**

## User

{% hint style="info" %}
**User Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](user.md#create) | [CreateUserRequest](user.md#createuserrequest) | [UserInfo](user.md#userinfo) |  |
| 2 | [update](user.md#update) | [UpdateUserRequest](user.md#updateuserrequest) | [UserInfo](user.md#userinfo) |  |
| 3 | [enable](user.md#enable) | [UserRequest](user.md#userrequest) | [UserInfo](user.md#userinfo) |  |
| 4 | [disable](user.md#disable) | [UserRequest](user.md#userrequest) | [UserInfo](user.md#userinfo) |  |
| 5 | [update\_role](user.md#update_role) | [UpdateUserRoleRequest](user.md#updateuserrolerequest) | [UserInfo](user.md#userinfo) |  |
| 6 | [delete](user.md#delete) | [UserRequest](user.md#userrequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 7 | [get](user.md#get) | [GetUserRequest](user.md#getuserrequest) | [UserInfo](user.md#userinfo) |  |
| 8 | [list](user.md#list) | [UserQuery](user.md#userquery) | [UsersInfo](user.md#usersinfo) |  |
| 9 | [stat](user.md#stat) | [UserStatQuery](user.md#userstatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |
| 10 | [find](user.md#find) | [FindUserQuery](user.md#finduserquery) | [FindUsersInfo](user.md#findusersinfo) |  |
| 11 | [sync](user.md#sync) | [UserRequest](user.md#userrequest) | [UserInfo](user.md#userinfo) |  |

### create

> **POST** /identity/v1/users

| Type | Message |
| :--- | :--- |
| Request | [CreateUserRequest](user.md#createuserrequest) |
| Response | [UserInfo](user.md#userinfo) |

### update

> **PUT** /identity/v1/users

| Type | Message |
| :--- | :--- |
| Request | [UpdateUserRequest](user.md#updateuserrequest) |
| Response | [UserInfo](user.md#userinfo) |

### enable

> **PUT** /identity/v1/user/{user\_id}/enable

| Type | Message |
| :--- | :--- |
| Request | [UserRequest](user.md#userrequest) |
| Response | [UserInfo](user.md#userinfo) |

### disable

> **PUT** /identity/v1/user/{user\_id}/disable

| Type | Message |
| :--- | :--- |
| Request | [UserRequest](user.md#userrequest) |
| Response | [UserInfo](user.md#userinfo) |

### update\_role

> **PUT** /identity/v1/user/{user\_id}/roles

| Type | Message |
| :--- | :--- |
| Request | [UpdateUserRoleRequest](user.md#updateuserrolerequest) |
| Response | [UserInfo](user.md#userinfo) |

### delete

> **DELETE** /identity/v1/users

| Type | Message |
| :--- | :--- |
| Request | [UserRequest](user.md#userrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### get

> **GET** /identity/v1/user/{user\_id}

| Type | Message |
| :--- | :--- |
| Request | [GetUserRequest](user.md#getuserrequest) |
| Response | [UserInfo](user.md#userinfo) |

### list

> **GET** /identity/v1/users
>
> **POST** /identity/v1/users/search

| Type | Message |
| :--- | :--- |
| Request | [UserQuery](user.md#userquery) |
| Response | [UsersInfo](user.md#usersinfo) |

### stat

> **POST** /identity/v1/users/stat

| Type | Message |
| :--- | :--- |
| Request | [UserStatQuery](user.md#userstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

### find

> **POST** /identity/v1/users/find

| Type | Message |
| :--- | :--- |
| Request | [FindUserQuery](user.md#finduserquery) |
| Response | [FindUsersInfo](user.md#findusersinfo) |

### sync

> **POST** /identity/v1/users/sync

| Type | Message |
| :--- | :--- |
| Request | [UserRequest](user.md#userrequest) |
| Response | [UserInfo](user.md#userinfo) |

## Message

### CreateUserRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user\_id | string |  | required |
| 2 | password | string |  | optional |
| 3 | name | string |  | optional |
| 4 | email | string |  | optional |
| 5 | mobile | string |  | optional |
| 6 | group | string |  | optional |
| 7 | language | string |  | optional |
| 8 | timezone | string |  | optional |
| 9 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 10 | domain\_id | string |  | optional |

### FindUserInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user\_id | string |  |  |
| 2 | name | string |  |  |
| 3 | email | string |  |  |
| 4 | mobile | string |  |  |
| 5 | group | string |  |  |
| 6 | state | string |  |  |

### FindUserQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | search | [FindUserSearch](user.md#findusersearch) |  |  |
| 2 | domain\_id | string |  |  |

### FindUserSearch

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user\_id | string |  |  |
| 2 | keyword | string |  |  |

### FindUsersInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [FindUserInfo](user.md#finduserinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### GetUserRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user\_id | string |  | required |
| 2 | domain\_id | string |  | required |
| 3 | only | string |  | optional |

### UpdateUserRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user\_id | string |  |  |
| 2 | password | string |  |  |
| 3 | name | string |  |  |
| 4 | email | string |  |  |
| 5 | mobile | string |  |  |
| 6 | group | string |  |  |
| 7 | language | string |  |  |
| 8 | timezone | string |  |  |
| 9 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 10 | domain\_id | string |  |  |

### UpdateUserRoleRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user\_id | string |  |  |
| 2 | roles | [google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) |  |  |
| 3 | domain\_id | string |  |  |

### UserInfo

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
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">
        <p>UserInfo.State</p>
        <ul>
          <li>NONE</li>
          <li>ENABLED</li>
          <li>DISABLED</li>
          <li>UNIDENTIFIED</li>
        </ul>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">email</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">mobile</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">group</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">language</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">timezone</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">roles</td>
      <td style="text-align:left"> <a href="user.md#roleinfo">RoleInfo</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">last_accessed_at</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
  </tbody>
</table>

### UserQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |  | optional |
| 2 | user\_id | string |  | optional |
| 3 | name | string |  | optional |
| 4 | state | string |  | optional |
| 5 | email | string |  | optional |
| 6 | mobile | string |  | optional |
| 7 | group | string |  | optional |
| 8 | role\_id | string |  | optional |
| 9 | project\_id | string |  | optional |
| 10 | project\_group\_id | string |  | optional |
| 11 | domain\_id | string |  | optional |

### UserRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user\_id | string |  | required |
| 2 | domain\_id | string |  | required |

### UserStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |  | required |
| 2 | domain\_id | string |  | required |

### UsersInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [UserInfo](user.md#userinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

