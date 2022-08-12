---
description: A Policy is a resource managing page access permissions. This resource can be used in all domains if it is defined in the `repository` microservice.
---
# Policy

>  **Package : spaceone.api.repository.v1**

## Policy

{% hint style="info" %}
**Policy Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](policy.md#create)|   [CreatePolicyRequest](policy.md#createpolicyrequest) |   [PolicyInfo](policy.md#policyinfo) |
| [**update**](policy.md#update)|   [UpdatePolicyRequest](policy.md#updatepolicyrequest) |   [PolicyInfo](policy.md#policyinfo) |
| [**delete**](policy.md#delete)|   [PolicyRequest](policy.md#policyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](policy.md#get)|   [GetRepositoryPolicyRequest](policy.md#getrepositorypolicyrequest) |   [PolicyInfo](policy.md#policyinfo) |
| [**list**](policy.md#list)|   [PolicyQuery](policy.md#policyquery) |   [PoliciesInfo](policy.md#policiesinfo) |
| [**stat**](policy.md#stat)|   [PolicyStatQuery](policy.md#policystatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /repository/v1/policies
>

> Creates a new Policy. The parameter `policy_id`, an identifier of Policy resources, can only include lowercase alphabets, numbers, and hyphens(-). The parameter `permissions` is a list type data describing page access permissions.

| Type | Message |
| :--- | :--- |
| Request | [CreatePolicyRequest](policy.md#createpolicyrequest) |
| Response |  [PolicyInfo](policy.md#policyinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "policy_id": "policy-custom-full-acess",
    "name": "Full Access",
    "permissions": [
        "*"
    ],
    "labels": [],
    "tags": {},
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "policy_id": "policy-custom-full-acess",
    "name": "Full Access",
    "state": "ENABLED",
    "permissions": [
        "*"
    ],
    "labels": [],
    "tags": {},
    "repository_info": {
        "repository_id": "repo-123456789012",
        "name": "Local",
        "repository_type": "local"
    },
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T06:45:04.582Z",
    "updated_at": "2022-01-01T06:45:04.582Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /repository/v1/policy/{policy}
>

> Updates a specific Policy. You can make changes in Policy settings, including `name`, `labels`, `tags`, and `permissions`. The parameter `policy_id` cannot be updated.

| Type | Message |
| :--- | :--- |
| Request | [UpdatePolicyRequest](policy.md#updatepolicyrequest) |
| Response |  [PolicyInfo](policy.md#policyinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "policy_id": "policy-custom-full-acess",
    "name": "Full Access",
    "permissions": [
        "*"
    ],
    "labels": [],
    "tags": {},
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "policy_id": "policy-custom-full-acess",
    "name": "Full Access",
    "state": "ENABLED",
    "permissions": [
        "*"
    ],
    "labels": [],
    "tags": {},
    "repository_info": {
        "repository_id": "repo-123456789012",
        "name": "Local",
        "repository_type": "local"
    },
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T06:45:04.582Z",
    "updated_at": "2022-01-01T06:45:04.582Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **DELETE** /repository/v1/policy/{policy}
>

> Deletes a specific Policy. You must specify the `policy_id` of the Policy to delete, as the `policy_id` is an identifier of Policy resources.

| Type | Message |
| :--- | :--- |
| Request | [PolicyRequest](policy.md#policyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "policy_id": "policy-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /repository/v1/policies/{policy}
>

> Gets a specific Policy. You must specify the `policy_id` of the Policy to get, as the `policy_id` is an identifier of Policy resources. You can use the parameter `repository_id` to limit the scope of the method to a specific Repository.

| Type | Message |
| :--- | :--- |
| Request | [GetRepositoryPolicyRequest](policy.md#getrepositorypolicyrequest) |
| Response |  [PolicyInfo](policy.md#policyinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "policy_id": "policy-123456789012",
    "repository_id": "repo-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "policy_id": "policy-123456789012",
    "name": "Full Access",
    "state": "ENABLED",
    "permissions": [
        "*"
    ],
    "labels": [],
    "tags": {},
    "repository_info": {
        "repository_id": "repo-123456789012",
        "name": "Local",
        "repository_type": "local"
    },
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T15:42:50.943Z",
    "updated_at": "2022-01-01T15:42:50.943Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /repository/v1/policies
>
> **POST** /repository/v1/policies/search


> Gets a list of all Policies in a specific Repository. The parameter `repository_id` is used as an identifier of a Repository to get its list of Policies. You can use a query to get a filtered list of Policies.

| Type | Message |
| :--- | :--- |
| Request | [PolicyQuery](policy.md#policyquery) |
| Response |  [PoliciesInfo](policy.md#policiesinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {},
    "repository_id": "repo-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "policy_id": "policy-123456789012",
            "name": "Full Access",
            "state": "ENABLED",
            "permissions": [
                "*"
            ],
            "labels": [],
            "tags": {},
            "repository_info": {
                "repository_id": "repo-123456789012",
                "name": "Local",
                "repository_type": "local"
            },
            "domain_id": "domain-123456789012",
            "created_at": "2022-01-01T15:42:50.943Z",
            "updated_at": "2022-01-01T15:42:50.943Z"
        },
        {
            "policy_id": "policy-987654321098",
            "name": "Identity Admin",
            "state": "ENABLED",
            "permissions": [
                "identity.*"
            ],
            "labels": [],
            "tags": {},
            "repository_info": {
                "repository_id": "repo-123456789012",
                "name": "Local",
                "repository_type": "local"
            },
            "domain_id": "domain-123456789012",
            "created_at": "2022-01-01T08:08:14.756Z",
            "updated_at": "2022-01-01T08:08:14.756Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /repository/v1/policies/stat
>


| Type | Message |
| :--- | :--- |
| Request | [PolicyStatQuery](policy.md#policystatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreatePolicyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| permissions |list of string|✔| |
| policy_id |string|✔| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| project_id |string|✘| |
| domain_id |string|✔| |

### GetRepositoryPolicyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| policy_id |string|✔| |
| domain_id |string|✔| |
| repository_id |string|✘| |
| only |list of string|✘| |

### PoliciesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of PolicyInfo](policy.md#policyinfo) | list of PolicyInfo|
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### PolicyInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">policy_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">permissions</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left">list of permissions</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">labels</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:left">list of labels</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">repository_info</td>
      <td style="text-align:left"><a href="policy.md#repositoryinfo">RepositoryInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### PolicyQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">policy_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">repository_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### PolicyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| policy_id |string|✔| |
| domain_id |string|✔| |

### PolicyStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| repository_id |string|✔| |
| domain_id |string|✔| |

### UpdatePolicyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| policy_id |string|✔| |
| name |string|✘| |
| permissions |list of string|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
