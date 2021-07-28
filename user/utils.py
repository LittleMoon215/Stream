import base64
import hmac
import hashlib


def create_key(HMAC_KEY, BASE_URL, SIGNATURE_QUERY_KEY_NAME, POLICY_QUERY_KEY_NAME, POLICY):
    baseUrl = BASE_URL
    policy = POLICY

    policyBase64 = base64.urlsafe_b64encode(policy.encode('utf-8'))
    policyBase64 = policyBase64.replace(b'=', b'')
    qsSeparator = "&" if ("?" in baseUrl) else "?"
    policyUrl = baseUrl + qsSeparator + POLICY_QUERY_KEY_NAME + "=" + policyBase64.decode('utf-8')

    signature = base64.urlsafe_b64encode(hmac.new(HMAC_KEY.encode(), policyUrl.encode(), hashlib.sha1).digest())
    signature = signature.replace(b'=', b'')
    signedUrl = policyUrl + '&' + SIGNATURE_QUERY_KEY_NAME + '=' + signature.decode('utf-8')
    return signedUrl
