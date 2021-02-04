#include<iostream>
#include<thread>
#include<mutex>
#include<stack>
#include<chrono>
#include<vector>
#include<cstring>
#include<cstdlib>
//ACTF{mult_thread_is_hard_to_control}

class usr_input{
private:
    std::mutex mutex;
    std::string str;
    bool mark;
public:
    void set_mark(bool value){
        mark = value;
    }
    bool get_mark() const{
        return mark;
    }
    void lock(){
        mutex.lock();
    }
    bool try_lock(){
        return mutex.try_lock();
    }
    size_t get_len() const{
        return str.length();
    }
    void unlock(){
        mutex.unlock();
    }
    void set_str(std::string&& input){
        str = std::move(input);
    }
    const char* get_c_str() const{
        return str.c_str();
    }
};

usr_input* usr;

void checker_thread_func()
{
    unsigned char buffer[0x200];
    unsigned char enc[] = {0xb7,0x8a,0xc8,0x29,0x39,0x78,0x9d,0xd7,0xfa,0x3e,0x40,0x6f,0xa8,0xc8,0xe1,0x37,0x79,0x90,0xbf,0xc0,0x1a,0x24,0x6a,0x8f,0xe1,0xe5,0x0b,0x68,0x69,0xb2,0xde,0xf7,0x24,0x46,0x90,0xb2,0x00};
    std::this_thread::sleep_for(std::chrono::milliseconds(100)); //利用输入事件，让reader先获得锁
    usr->lock();
    int &&len = usr->get_len();
    if (len > 0x150){
        usr->unlock();
        return;
    }
    strcpy((char *)buffer,usr->get_c_str());
    for (int i = 0; i < len; ++i){
        buffer[i] ^= (45 * i + 9) % 0x100;
        buffer[i] = ~buffer[i];
    }
    for (int i = 0; i < len; ++i){
        if(buffer[i] - enc[i]){
            usr->set_mark(false);
        }
    }
    usr->unlock();
    return;
}

void reader_thread_func(){
    usr->lock();
    std::string buffer;
    std::cin >> buffer;
    usr->set_str(std::move(buffer));
    usr->set_mark(true);
    usr->unlock();
    return;
}

int main(){
    usr = new usr_input();
    usr->lock();
    std::thread *reader = new std::thread(reader_thread_func);
    std::thread* checker= new std::thread(checker_thread_func);
    std::cout << "MultThread Program~\n"
                 "Could you reverse it?\n"
                 "Please Input:\n";
    usr->unlock();
    reader->join();
    checker->join();
    delete reader;
    delete checker;
    usr->lock();
    if(usr->get_mark()){
        std::cout << "success!\n";
    }
    else{
        std::cout << "fail\n";
    }
    system("timeout 5");
    usr->unlock();
    delete usr;
    return 0;
}