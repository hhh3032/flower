#!/bin/bash
set -e

case "$1" in
  e2e-bare-https | e2e-bare-auth)
    ./generate.sh
    server_arg="--ssl-ca-certfile certificates/ca.crt --ssl-certfile certificates/server.pem --ssl-keyfile certificates/server.key"
    client_arg="--root-certificates certificates/ca.crt"
    server_dir="./"
    ;;
  *)
    server_arg="--insecure"
    client_arg="--insecure"
    server_dir="./"
    ;;
esac

case "$2" in
  rest)
    rest_arg_superlink="--fleet-api-type rest"
    rest_arg_supernode="--rest"
    server_address="http://localhost:9095"
    server_app_address="127.0.0.1:9091"
    db_arg="--database :flwr-in-memory-state:"
    server_auth=""
    client_auth_1=""
    client_auth_2=""
    ;;
  sqlite)
    rest_arg_superlink=""
    rest_arg_supernode=""
    server_address="127.0.0.1:9092"
    server_app_address="127.0.0.1:9091"
    db_arg="--database $(date +%s).db"
    server_auth=""
    client_auth_1=""
    client_auth_2=""
    ;;
  client-auth)
    rest_arg_superlink=""
    rest_arg_supernode=""
    server_address="127.0.0.1:9092"
    server_app_address="127.0.0.1:9091"
    db_arg="--database :flwr-in-memory-state:"
    server_auth="--auth-list-public-keys keys/client_public_keys.csv --auth-superlink-private-key keys/server_credentials --auth-superlink-public-key keys/server_credentials.pub"
    client_auth_1="--auth-supernode-private-key keys/client_credentials_1 --auth-supernode-public-key keys/client_credentials_1.pub"
    client_auth_2="--auth-supernode-private-key keys/client_credentials_2 --auth-supernode-public-key keys/client_credentials_2.pub"
    ;;
  *)
    rest_arg_superlink=""
    rest_arg_supernode=""
    server_address="127.0.0.1:9092"
    server_app_address="127.0.0.1:9091"
    db_arg="--database :flwr-in-memory-state:"
    server_auth=""
    client_auth_1=""
    client_auth_2=""
    ;;
esac

timeout 2m flower-superlink $server_arg $db_arg $rest_arg_superlink $server_auth --isolation="process" &
sl_pid=$!
sleep 3

timeout 2m flower-supernode ./ $client_arg $rest_arg_supernode --superlink $server_address $client_auth_1 &
cl1_pid=$!
sleep 3

timeout 2m flower-supernode ./ $client_arg $rest_arg_supernode --superlink $server_address $client_auth_2 &
cl2_pid=$!
sleep 3

timeout 2m flower-server-app $server_dir $client_arg --superlink $server_app_address &
pid=$!

wait $pid
res=$?

if [[ "$res" = "0" ]];
  then echo "Training worked correctly"; kill $cl1_pid; kill $cl2_pid; kill $sl_pid;
  else echo "Training had an issue" && exit 1;
fi
