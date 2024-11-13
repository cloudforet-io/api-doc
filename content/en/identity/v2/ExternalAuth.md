---
title: "ExternalAuth"
linkTitle: "ExternalAuth"
weight: 3
bookFlatSection: true
---
# [ExternalAuth](#ExternalAuth)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## ExternalAuth





**ExternalAuth Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**set**](./ExternalAuth#set) | [SetExternalAuthRequest](ExternalAuth#setexternalauthrequest) | [ExternalAuthInfo](ExternalAuth#externalauthinfo) |
| [**unset**](./ExternalAuth#unset) | [ExternalAuthRequest](ExternalAuth#externalauthrequest) | [ExternalAuthInfo](ExternalAuth#externalauthinfo) |
| [**get**](./ExternalAuth#get) | [ExternalAuthRequest](ExternalAuth#externalauthrequest) | [ExternalAuthInfo](ExternalAuth#externalauthinfo) |



    
<br>

### set

Google OAuth2, Keycloak OIDC, SAML are supported as external authentication.



> **POST** /identity/v2/external-auth/set
>





 {{< tabs " set " >}}

 {{< tab "Request Example" >}}



[SetExternalAuthRequest](./ExternalAuth#setexternalauthrequest)

* **plugin_info** (PluginRequest)   `Required` 





{{< highlight json >}}
{
 "plugin_id": "plugin-googleoauth2-identity-auth",
 "upgrade_mode": "AUTO",
 "options": {
     "client_id": "client_id",
     "protocol": "oauth2",
     "identity_provider": "google",
     "validator": "gmail.com"
  }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ExternalAuthInfo](#EXTERNALAUTHINFO)
* **domain_id** (string)   `Required` 

* **state** (State)   `Required` 

* **plugin_info** (PluginInfo)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
 "domain_id": "domain-123456",
 "plugin_info": {
     "metadata": {
         "authorization_endpoint": "https://www.googleapis.com",
         "client_id": "client_id",
         "identity_provider": "google",
         "protocol": "oauth2",
         "token_endpoint": "https://www.googleapis.com/oauth2/v2/tokeninfo",
         "userinfo_endpoint": "https://www.googleapis.com/oauth2/v3/userinfo",
         "validator": "gmail.com"
     },
     "options": {
         "client_id": "client_id",
         "identity_provider": "google",
         "protocol": "oauth2",
         "validator": "gmail.com"
     },
     "plugin_id": "plugin-googleoauth2-identity-auth",
     "upgrade_mode": "AUTO",
     "version": "1.1.3"
 }
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### unset

Unset external authentication information.



> **POST** /identity/v2/external-auth/unset
>





 {{< tabs " unset " >}}

 {{< tab "Request Example" >}}



[ExternalAuthRequest](./ExternalAuth#externalauthrequest)




{{< highlight json >}}
{
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ExternalAuthInfo](#EXTERNALAUTHINFO)
* **domain_id** (string)   `Required` 

* **state** (State)   `Required` 

* **plugin_info** (PluginInfo)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
 "domain_id": "domain-123456",
 "plugin_info": {
     "metadata": {
         "authorization_endpoint": "https://www.googleapis.com",
         "client_id": "client_id",
         "identity_provider": "google",
         "protocol": "oauth2",
         "token_endpoint": "https://www.googleapis.com/oauth2/v2/tokeninfo",
         "userinfo_endpoint": "https://www.googleapis.com/oauth2/v3/userinfo",
         "validator": "gmail.com"
     },
     "options": {
         "client_id": "client_id",
         "identity_provider": "google",
         "protocol": "oauth2",
         "validator": "gmail.com"
     },
     "plugin_id": "plugin-googleoauth2-identity-auth",
     "upgrade_mode": "AUTO",
     "version": "1.1.3"
 }
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get

Get external authentication information.



> **POST** /identity/v2/external-auth/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[ExternalAuthRequest](./ExternalAuth#externalauthrequest)




{{< highlight json >}}
{
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ExternalAuthInfo](#EXTERNALAUTHINFO)
* **domain_id** (string)   `Required` 

* **state** (State)   `Required` 

* **plugin_info** (PluginInfo)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
 "domain_id": "domain-123456",
 "plugin_info": {
     "metadata": {
         "authorization_endpoint": "https://www.googleapis.com",
         "client_id": "client_id",
         "identity_provider": "google",
         "protocol": "oauth2",
         "token_endpoint": "https://www.googleapis.com/oauth2/v2/tokeninfo",
         "userinfo_endpoint": "https://www.googleapis.com/oauth2/v3/userinfo",
         "validator": "gmail.com"
     },
     "options": {
         "client_id": "client_id",
         "identity_provider": "google",
         "protocol": "oauth2",
         "validator": "gmail.com"
     },
     "plugin_id": "plugin-googleoauth2-identity-auth",
     "upgrade_mode": "AUTO",
     "version": "1.1.3"
 }
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    


<br>
<br>

## Message



### ExternalAuthInfo
* **domain_id** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **plugin_info** (PluginInfo)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### ExternalAuthRequest<br>

### SetExternalAuthRequest
* **plugin_info** (PluginRequest)   `Required` 

    <br>
