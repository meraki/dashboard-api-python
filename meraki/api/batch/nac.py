import urllib


class ActionBatchNac(object):
    def __init__(self):
        super(ActionBatchNac, self).__init__()
        


    def createOrganizationNacCertificatesAuthoritiesCrl(self, organizationId: str, caId: str, content: str, isDelta: bool):
        """
        **Create a new CRL (either base or delta) for an existing CA**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-certificates-authorities-crl

        - organizationId (string): Organization ID
        - caId (string): ID of the CRL issuer
        - content (string): CRL content in PEM format
        - isDelta (boolean): Whether it's a delta CRL or not
        """

        kwargs = locals()

        metadata = {
            'tags': ['nac', 'configure', 'certificates', 'authorities', 'crls'],
            'operation': 'createOrganizationNacCertificatesAuthoritiesCrl'
        }
        resource = f'/organizations/{organizationId}/nac/certificates/authorities/crls'

        body_params = ['caId', 'content', 'isDelta', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        



