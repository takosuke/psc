server {
    listen   80;
    server_name {{ domain_name }};
    return 301 http://www.{{ domain_name }}$request_uri;
    }

server {
    listen       80;
    server_name  www.{{ domain_name }};
    root {{ webapps_dir }}/{{ app_name }}/html;
    access_log {{ webapps_dir}}/{{ app_name }}/log/nginx/{{ domain_name }}.access.log;
    error_log {{ webapps_dir}}/{{ app_name }}/log/nginx/{{ domain_name }}.error.log info;

    location /static/ {
    alias {{ webapps_dir }}/{{ app_name }}/{{ static_root }}/;
    expires 30d;
    }

    location /media/ {
    alias {{ webapps_dir }}/{{ app_name }}/{{ media_root }}/;
    expires 30d;
    }
    location / {
    include uwsgi_params;
    uwsgi_pass unix:/tmp/{{ app_name }}.sock;
    }
}

