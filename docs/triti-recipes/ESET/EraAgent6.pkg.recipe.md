# EraAgent6.pkg.recipe

            _Last updated 2021-12-23 19:58:07Z_

            - **Description**: Downloads the ESET Remote Administrator Agent.

Override this recipe and replace the Input values below with values for your
ERA installation.

eraa_server_hostname: Hostname of your ESET Remote Administrator server.
eraa_server_port: TCP port for your ERA server.
eraa_peer_cert_b64: Base64 encoded peer certificate for your agemts. Obtain 
    from Admin--Certificates--Peer Certificates--click on Agent certificate
    --Export as Base64.
eraa_ca_cert_b64: Base64 encoded CA public key. Obtain from Admin--Certificates
    Certification Authorities--click on ERA Certification authority
    --Export Public Key as Base64.

Optional Input variables
eraa_peer_cert_pwd: Password for the peer certiticate.


            - **Identifier**: `com.github.triti.pkg.EraAgent6`

            - **Parent Recipes**: `com.github.triti.download.EraAgent6`