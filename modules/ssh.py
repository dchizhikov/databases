#os.system('pip install paramiko')
import paramiko

def create_ssh_tunnel(ssh_host, ssh_user, ssh_password, remote_bind_address, local_bind_port):
  """Создание SSH-туннеля."""
  try:
      # Создаем SSH-клиент
      ssh_client = paramiko.SSHClient()
      ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

      # Подключаемся к SSH-серверу
      ssh_client.connect(ssh_host, username=ssh_user, password=ssh_password, port=22)

      # Создаем туннель (локальный хост, локальный порт, удаленный хост, удаленный порт)
      transport = ssh_client.get_transport()
      transport.request_port_forward('localhost:0', local_bind_port, remote_bind_address[0] + ':' + str(remote_bind_address[1]))

      print(f"SSH туннель установлен на порт {local_bind_port}")
      return ssh_client

  except Exception as e:
      print(f"Ошибка при создании SSH-туннеля: {e}")
      return None