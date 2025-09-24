# Microsoft Active Directory
Microsoft Active Directory (AD) is a directory service developed by Microsoft for Windows domain networks. It provides centralized authentication, authorization, and management of users, computers, and other resources within an organization. AD enables administrators to manage permissions and access to networked resources efficiently using features like domains, organizational units (OUs), group policies, and trust relationships.

## Protocols Used by Active Directory

Active Directory relies on several key protocols to provide its services:

- **LDAP (Lightweight Directory Access Protocol):** Used for querying and modifying items in the directory.
- **Kerberos:** Provides secure authentication for users and computers.
- **DNS (Domain Name System):** Resolves domain names to IP addresses, essential for locating domain controllers.
- **SMB (Server Message Block):** Used for file sharing and communication between computers.
- **NTLM (NT LAN Manager):** Legacy authentication protocol, still supported for backward compatibility.
- **Global Catalog:** Uses LDAP to provide information about objects in the directory across domains.

These protocols work together to enable secure authentication, resource access, and directory management in Active Directory environments.

## Authentication & Authorization
- authentication : who the individual ( user id and password)
- authorization : what all permissions you have.

## Single Sign on (SSO)
 - One identity gets you access to many resources. 

## Features of Entra ID
 - Issues a token that proves who you are 
 - That token is trusted by all other applications in your company
 - Instead of asking for your password again, it checks your token
 - Authenticate once, trusted everywhere. 

## Entra Conditional Access
- conditioning suspicious logins.

## Multi-Factor Authentication
 - Require 2 or more pieces of evidence (factors) in order to log in.

## Passwordless Authentication

## Role-Based Access Control ( RBAC)
 - Principle of Least Privilege 
 - Developer
 - Operations
 - IT Security
 - Assign users to those roles.
 - Try to avoid exceptions where User X has admin privileges that you dont't expect. 
 - Three Basic Roles 
    - Reader - cannot make any changes ( edit, delete ...and so on)
    - Contributor - you are administrator but you cannot make others administrators.
    - Owner  - can assign permissions to others.


## Zero Trust Model 
 - protecting the border - the boundary between the company and the public internet(DMZ)
 - Everything inside the corporate network as assumed safe. 
 - Can't trust any connections regardless where it comes from 
 - force everyone to prove their identity.
 - verify explicitly
 - use least privileged access.
 - assume breach.
 - Just in time (JIT) access.
 - Just enough access ( JEA)

## Defence in Depth
 - Security Layers 
   - Data , virtual network endpoint
   - application - api management
   - compute , limit remote desktop access, windows update,
   - network - NSG, use of subnets, deny by default
   - perimeter - firewalls, DDoS
   - Indentiy and access - EntraID
   - Physical - door locks 

## Microsoft Defender for Cloud
 - Security Posture Management 
 - Defender Plans
 