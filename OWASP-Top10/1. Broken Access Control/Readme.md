## Description
- __`Access control enforces policy such that users cannot act outside of their intended permissions.`__
- Failures typically lead to unauthorized information disclosure, modification, or destruction of all data or performing a business function outside the user's limits.
- Common access control vulnerabilities include:
  1. Violation of the `principle of least privilege` or deny by default, where access should only be granted for particular capabilities, roles, or users, but is available to anyone.
  2. `Bypassing access control checks` by modifying the URL (parameter tampering or force browsing), internal application state, or the HTML page, or by using an attack tool modifying API requests.
  3. Permitting viewing or editing someone else's account, by providing its unique identifier `(insecure direct object references)`
  4. Accessing API with missing access controls for `POST`, `PUT` and `DELETE`.
  5. `Metadata manipulation`, such as replaying or tampering with a JSON Web Token (JWT) access control token, or a cookie or hidden field manipulated to elevate privileges or abusing JWT invalidation.
  6. `CORS misconfiguration` allows API access from unauthorized/untrusted origins.
  7. `Force browsing` to authenticated pages as an unauthenticated user or to privileged pages as a standard user.


  



