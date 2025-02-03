# <```OAuth 2.0```> 

para la autenticación y la autorización. <``Binance``> admite escenarios 

## «%Binance%» para obtener el scopes %\``A©®``/%{Centro de desarrolladores de Binance} 

# Para aplicaciones web,  se consulta la sección ```“Flujo del código de autorización" 

# Para aplicaciones basadas en navegador, así como aplicaciones móviles y nativas, consulte la sección <"Flujo PCKE" .>

# GET https://accounts.binance.com/en/oauth/authorize? response_type=code& client_id=YOUR_CLIENT_ID& redirect_uri=YOUR_REDIRECT_URI& state=CSRF_TOKEN& scope=SCOPES <input data-testid="no-aria-invalid" /><input data-testid="aria-invalid" aria-invalid />

# <input data-testid="aria-invalid-value" aria-invalid="true" /><input data-testid="aria-invalid-false" aria-invalid="false" /> 

# <form data-testid="valid-form">
  <input />
</form>


<form data-testid="invalid-form">
  <input required />
</form>expect(getByTestId('no-aria-invalid')).toBeValid()
expect(getByTestId('aria-invalid')).not.toBeValid()
expect(getByTestId('aria-invalid-value')).not.toBeValid()
expect(getByTestId('aria-invalid-false')).toBeValid()


expect(getByTestId('valid-form')).toBeValid()
expect(getByTestId('invalid-form')).not.toBeValid()toBeVisible()expect(getByTestId('required-input')).toBeRequired()
expect(getByTestId('aria-required-input')).toBeRequired()
expect(getByTestId('conflicted-input')).toBeRequired()
expect(getByTestId('aria-not-required-input')).not.toBeRequired()
expect(getByTestId('optional-input')).not.toBeRequired()
expect(getByTestId('unsupported-type')).not.toBeRequired()
expect(getByTestId('select')).toBeRequired()
expect(getByTestId('textarea')).toBeRequired()
expect(getByTestId('supported-role')).not.toBeRequired()
expect(getByTestId('supported-role-aria')).toBeRequired()<input data-testid="required-input" required />
<input data-testid="aria-required-input" aria-required="true" />
<input data-testid="conflicted-input" required aria-required="false" />
<input data-testid="aria-not-required-input" aria-required="false" />
<input data-testid="optional-input" />
<input data-testid="unsupported-type" type="image" required />
<select data-testid="select" required></select>
<textarea data-testid="textarea" required></textarea>
<div data-testid="supported-role" role="tree" required></div>
<div data-testid="supported-role-aria" role="tree" aria-required="true"></div>expect(getByTestId('no-aria-invalid')).not.toBeInvalid()
expect(getByTestId('aria-invalid')).toBeInvalid()
expect(getByTestId('aria-invalid-value')).toBeInvalid()
expect(getByTestId('aria-invalid-false')).not.toBeInvalid()


expect(getByTestId('valid-form')).not.toBeInvalid()
expect(getByTestId('invalid-form')).toBeInvalid()toBeInvalid()expect(
  getByTestId(document.documentElement, 'html-element'),
).toBeInTheDocument()
expect(getByTestId(document.documentElement, 'svg-element')).toBeInTheDocument()
expect(
  queryByTestId(document.documentElement, 'does-not-exist'),
).not.toBeInTheDocument()<span data-testid="not-empty"><span data-testid="empty"></span></span>
<span data-testid="with-whitespace"> </span>
<span data-testid="with-comment"><!-- comment --></span>expect(getByTestId('empty')).toBeEmptyDOMElement()
expect(getByTestId('not-empty')).not.toBeEmptyDOMElement()
expect(getByTestId('with-whitespace')).not.toBeEmptyDOMElement()<span data-testid="html-element"><span>Html Element</span></span>
<svg data-testid="svg-element"></svg>


Descripción
response_type
Valor requeridocode
client_id
Obligatorio El ID de cliente de su aplicación.
redirect_uri
requerido La URL de su aplicación web a la que se redirigirá a los usuarios después de la autorización. Este valor debe estar codificado en URL.
state
Opcional El token CSRF para protegerse contra ataques CSRF (falsificación de solicitud entre sitios).
scope
requerido Lista de ámbitos a los que su aplicación solicita acceso, ,separados por comas ( ).

A continuación se muestra un ejemplo de una URL de autorización:
GET https://accounts.binance.com/en/oauth/authorize?
   response_type=code&
   client_id=a28f296f2cbe6c64b4d5dec24735d39b1b6fffcf&
   redirect_uri=https%3A%2F%2Fdomain.com%2Foauth%2Fcallback&
   state=377f36a4557ab5935b36&
   scope=user:openId,create:apikey
redirect_uricon un parámetro de autorización temporal code.
Si especificó un stateparámetro en el paso 1, también se incluirá. Si genera una cadena aleatoria o codifica el hash de una cookie u otro valor que captura el cliente state, puede validar la respuesta para garantizar además que la solicitud y la respuesta se originaron en el mismo navegador, lo que brinda protección contra ataques como la falsificación de solicitudes entre sitios.
Ejemplo de redirección:
GET https://domain.com/oauth/callback?
   code=cf6941ae8918b6a008f1377f36a4557ab5935b36&
   state=377f36a4557ab5935b36
state
## ``` tokens ```


# code, puede intercambiar la autorización codepor un token de acceso, lo que se puede hacer mediante una llamada POST:




# POST https://accounts.binance.com/oauth/token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=authorization_code&code=STEP3_CODE&redirect_uri=YOUR_REDIRECT_URI
Parámetro
Descripción
grant_type
Valor requeridoauthorization_code
code
Código de retorno requerido del paso 3
client_id
requerido El ID de cliente de su aplicación.
client_secret
requerido El secreto del cliente de su aplicación.
redirect_uri
requerido La URL de su aplicación web a la que se redirigirá a los usuarios después de la autorización. Este valor debe estar codificado en URL.

Ejemplo de llamada POST:
curl https://accounts.binance.com/oauth/token \
 -X POST
 -d 'client_id=je-client&client_secret=je-client-secret&grant_type=authorization_code&code=95OfIm&redirect_uri=https%3A%2F%2Fdomain.com%2Foauth%2Fcallback'
Después de una solicitud exitosa, se devolverá algo válido access_tokenen la respuesta y será inválido si excede el expires_intiempo en la respuesta, que es en segundos.
He aquí un ejemplo de respuesta:
{
 "access_token": "83f2bf51-a2c4-4c2e-b7c4-46cef6a8dba5",
 "refresh_token": "fb5587ee-d9cf-4cb5-a586-4aed72cc9bea",
 "scope": "read",
 "token_type": "bearer",
 "expires_in": 30714
}
Paso 5. Intercambio de tokens de actualización por tokens
Si su token de acceso ha expirado, puede usarlo refresh_tokenpara obtener un nuevo token de acceso, lo cual puede hacerse mediante una llamada POST:
POST https://accounts.binance.com/oauth/token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=refresh_token&refresh_token=STEP4_REFRESH_TOKEN
Parámetro
Descripción
grant_type
 Valor  requeridorefresh_token
refresh_token
 Token de actualización requerido del paso 4
client_id
requerido  El ID de cliente de su aplicación.
client_secret
requerido  El secreto del cliente de su aplicación.
Ejemplo de llamada POST:



curl https://accounts.binance.com/oauth/token \
 -X POST
 -d 'client_id=je-client&client_secret=je-client-secret&grant_type=refresh_token&refresh_token=95OfIm
Después de una solicitud exitosa, se devolverá algo válido  access_token en la respuesta y será inválido si excede el expires_intiempo en la respuesta, que es en segundos.
He aquí un ejemplo de respuesta:
{
 "access_token": "83f2bf51-a2c4-4c2e-b7c4-46cef6a8dba5",
 "refresh_token": "fb5587ee-d9cf-4cb5-a586-4aed72cc9bea",
 "scope": "read",
 "token_type": "bearer",
 "expires_in": 30714
}
Paso 6. Llamar a las API
Una vez que tengas un access_token, puedes realizar tu primera llamada API:
curl 'https://www.binanceapis.com/oauth-api/v1/user-info' \
--header 'Authorization: Bearer {access_token}'
Respuesta:
{
 "code": "000000",
 "message": null,
 "data": {
   "userId": "e10e20b7f20947e7bd206b15ce3dae90",
   "email": "xx@xx.com"
 },
 "success": true
}
2. Flujo de
La extensión PKCE evita un ataque en el que un cliente malintencionado intercepta el código de autorización y lo intercambia por un token de acceso, al proporcionar al servidor de autorización una forma de verificar que la misma instancia del cliente que intercambia el código de autorización es la misma que inició el flujo. Para obtener más detalles, consulte https://tools.ietf.org/html/rfc7636
Paso 1. Redirigir a los usuarios para solicitar acceso a Binance y establecer parámetros de autorización .
GET https://accounts.binance.com/en/oauth/authorize?
   response_type=code&
   client_id=YOUR_CLIENT_ID&
   redirect_uri=YOUR_REDIRECT_URI&
   state=CSRF_TOKEN&
   scope=SCOPES&
   code_challenge=CODE_CHALLENGE&
   code_challenge_method=S256

Los retornos de carro del ejemplo anterior son solo para facilitar la lectura y deben eliminarse en el mundo real, así como los siguientes ejemplos.
Al redirigir a un usuario a Binance para autorizar el acceso a su aplicación, el primer paso es crear la solicitud de autorización. Debe crear y almacenar un nuevo código PKCE code_verifier, que también se utilizará en el PASO 4.
Aquí hay un ejemplo de código generado por javascript_verifier
// Generate a secure random string using the browser crypto functions
function generateRandomString() {
 var array = new Uint32Array(28);
 window.crypto.getRandomValues(array);
 return Array.from(array, (dec) => ("0" + dec.toString(16)).substr(-2)).join(
   ""
 );
}
Parámetros
Descripción
response_type
Valor requeridocode
client_id
Obligatorio El ID de cliente de su aplicación.
redirect_uri
requerido La URL de su aplicación web a la que se redirigirá a los usuarios después de la autorización. Este valor debe estar codificado en URL.
state
Opcional El token CSRF para protegerse contra ataques CSRF (falsificación de solicitud entre sitios).
scope
requerido Lista de ámbitos a los que su aplicación solicita acceso, ,separados por comas ( ).
code_challenge
Hash requerido y código URL base64 de code_verifier

Aquí hay un ejemplo de código de generación de JavaScript_challenge
// Calculate the SHA256 hash of the input text.
function sha256(code_verifier) {
 const encoder = new TextEncoder();
 const data = encoder.encode(code_verifier);
 return window.crypto.subtle.digest("SHA-256", data);
}


// Base64-urlencodes the input string
function base64urlencode(hashed) {
 return btoa(String.fromCharCode.apply(null, new Uint8Array(hashed)))
   .replace(/\+/g, "-")
   .replace(/\//g, "_")
   .replace(/=+$/, "");
}


// Return the base64-urlencoded sha256 hash for the PKCE challenge
async function generateCodeChallenge(code_verifier) {
 hashed = await sha256(code_verifier);
 return base64urlencode(hashed);
}
A continuación se muestra un ejemplo de una URL de autorización:
GET https://accounts.binance.com/en/oauth/authorize?
   response_type=code&
   client_id=a28f296f2cbe6c64b4d5dec24735d39b1b6fffcf&
   redirect_uri=https%3A%2F%2Fdomain.com%2Foauth%2Fcallback&
   state=377f36a4557ab5935b36&
   scope=user:openId,create:apikey&
   code_challenge=ARU184muFVaDi3LObH5YTZSxqA5ZdYPLspCl7wFwV0U
   code_challenge_method=S256
Paso 2. Binance solicita el consentimiento
En este paso, el usuario decide si concede a su aplicación el acceso solicitado. En esta etapa, Binance muestra una ventana de consentimiento que muestra el nombre de su aplicación y los servicios de la API de Binance a los que solicita permiso para acceder con las credenciales de autorización del usuario. El usuario puede entonces dar su consentimiento o rechazar el acceso a su aplicación.
Su aplicación no necesita hacer nada en esta etapa ya que espera que el servidor OAuth 2.0 de Binance la redireccione nuevamente.
Paso 3. Binance te redirecciona a tu aplicación
Si el usuario aprueba su solicitud, el servidor OAuth de Binance lo redireccionará nuevamente a usted redirect_uricon un parámetro de autorización temporal code.
Si especificó un stateparámetro en el paso 1, también se incluirá. Si genera una cadena aleatoria o codifica el hash de una cookie u otro valor que captura el cliente state, puede validar la respuesta para garantizar además que la solicitud y la respuesta se originaron en el mismo navegador, lo que brinda protección contra ataques como la falsificación de solicitudes entre sitios.
Ejemplo de redirección:
GET https://domain.com/oauth/callback?
   code=cf6941ae8918b6a008f1377f36a4557ab5935b36&
   state=377f36a4557ab5935b36
statees el mismo que el del paso 1
Paso 4. Intercambio de códigos de autorización por tokens
Una vez que su aplicación recibe la autorización code, puede intercambiar la autorización codepor un token de acceso, lo que se puede hacer mediante una llamada POST:
POST https://accounts.binance.com/oauth/token?client_id=YOUR_CLIENT_ID&code_verifier=STEP1_CODE_VERIFIER&grant_type=authorization_code&code=STEP3_CODE&redirect_uri=YOUR_REDIRECT_URI
Parámetro
Descripción
grant_type
Valor requeridoauthorization_code
code
Código de retorno requerido del paso 3
client_id
requerido El ID de cliente de su aplicación.
code_verifier
requerido El código secreto aleatorio creado y almacenado en STEP1
redirect_uri
requerido La URL de su aplicación web a la que se redirigirá a los usuarios después de la autorización. Este valor debe estar codificado en URL.

Ejemplo de llamada POST:
curl https://accounts.binance.com/oauth/token \
 -X POST
 -d 'client_id=je-client&code_verifier=65a4ecce1fe857067bec7a6887529531831ebe38e32da95fe0f322a2&grant_type=authorization_code&code=95OfIm&redirect_uri=https%3A%2F%2Fdomain.com%2Foauth%2Fcallback'
Después de una solicitud exitosa, se devolverá algo válido access_tokenen la respuesta y será inválido si excede el expires_intiempo en la respuesta, que es en segundos.
He aquí un ejemplo de respuesta:
{
 "access_token": "83f2bf51-a2c4-4c2e-b7c4-46cef6a8dba5",
 "refresh_token": "fb5587ee-d9cf-4cb5-a586-4aed72cc9bea",
 "scope": "read",
 "token_type": "bearer",
 "expires_in": 30714
}
Paso 5. Intercambio de tokens de actualización por tokens
Si su token de acceso ha expirado, puede usarlo refresh_tokenpara obtener un nuevo token de acceso, lo cual puede hacerse mediante una llamada POST:
POST https://accounts.binance.com/oauth/token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=refresh_token&refresh_token=STEP4_REFRESH_TOKEN
Parámetro
Descripción
grant_type
 Valor  requeridorefresh_token
refresh_token
 Token de actualización requerido del paso 4
client_id
requerido  El ID de cliente de su aplicación.
client_secret
requerido  El secreto del cliente de su aplicación.
Ejemplo de llamada POST:



curl https://accounts.binance.com/oauth/token \
 -X POST
 -merge-app.js'client_id=je-client&client_secret=je-client-secret&grant_type=refresh_token&refresh_token=95OfIm
devolverá algo válido  access_token en la respuesta y será inválido si excede el expires_intiempo en la respuesta, que es en segundos.
He aquí un ejemplo de respuesta:
{
 "access_token": "83f2bf51-a2c4-4c2e-b7c4-46cef6a8dba5",
 "refresh_token": "fb5587ee-d9cf-4cb5-a586-4aed72cc9bea",
 "scope": "read",
 "token_type": "bearer",
 "expires_in": 30714
} access_token, puedes realizar tu primera llamada API:
curl 'https://www.binanceapis.com/oauth-api/v1/user-info' \
--header 'Authorization: Bearer {access_token}'
Respuesta:
{
 "code": "000000",
 "message": null,
 "data": {
   "userId": "e10e20b7f20947e7bd206b15ce3dae90",
   "email": "xx@xx.com"
 },
 "success": true
}
