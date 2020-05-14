#include <acmq_msg.h>

AcmqSender producer;
int main(int argc, char *argv[])
{

    activemq::library::ActiveMQCPP::initializeLibrary();
    std::cout << "=====================================================\n";
    std::cout << "Starting produce message:" << std::endl;
    std::cout << "-----------------------------------------------------\n";

    //std::string brokerURI ="failover://(tcp://192.175.1.11:61616)";
    std::string brokerURI = "tcp://192.175.1.11:61616";
    std::string destURI = "a_0514";
    bool useTopics = false;

    while (1)
    {
        producer.init(brokerURI, destURI, useTopics);
        bool b;
        //b = producer.sendMessage("hello world from test.zhaogang");
        b = producer.sendMessage("ÄãºÃ hello world from abcde");
        if (b == false)
        {
            std::cout << "send failed!" << std::endl;
        }
        producer.close();
        sleep(5);
    }
    producer.init(brokerURI, destURI, useTopics);
    bool b = producer.sendMessage("hello world 111 from test.zhaogang");
    if (b == false)
    {
        std::cout << "send failed!" << std::endl;
    }
    producer.close();

    std::cout << "-----------------------------------------------------\n";
    std::cout << "Finished test" << std::endl;
    std::cout << "=====================================================\n";

    activemq::library::ActiveMQCPP::shutdownLibrary();
}
