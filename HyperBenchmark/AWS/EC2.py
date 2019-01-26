import boto3
import paramiko
import logging as log
import watchtower
logFormatter = log.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")


class Instance:
    def __init__(self, imageid='ami-02b15491d756c53d1'):
        self.logger = log.getLogger(type(self).__name__)
        consoleHandler = log.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        ec2Handler = watchtower.CloudWatchLogHandler()
        ec2Handler.setFormatter(logFormatter)
        self.logger.addHandler(consoleHandler)
        self.logger.addHandler(ec2Handler)
        session = boto3.Session(region_name="us-west-2") #Oregon
        self.imageid = imageid
        self.ec2 = session.resource('ec2')
        self.instance = None
        return

    def create_instance(self, test=False):
        instance_info = self.ec2.create_instances(
            ImageId=self.imageid,
            DryRun=test,
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro'#'p2.xlarge'
        )
        self.instanceid = instance_info['StartingInstances']['InstanceId']

    def terminate(self):
        self.ec2.instances.filter(InstanceIds=[self.instanceid]).terminate()

    def __del__(self):
        """Destroy the instance"""
        self.logger.error(f'Instance is not terminated delete, auto terminating {self.instanceid}')
        self.terminate()
        self.logger.error('instance terminated')

    def execue(self, command):
        key = paramiko.RSAKey.from_private_key_file(path/to/mykey.pem)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Connect/ssh to an instance
        try:
            # Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2
            client.connect(hostname=instance_ip, username="ubuntu", pkey=key)

            # Execute a command(cmd) after connecting/ssh to an instance
            stdin, stdout, stderr = client.exec_command(command)
            print (stdout.read())

            # close the client connection once the job is done
            client.close()
            break

        except Exception, e:
            print e
