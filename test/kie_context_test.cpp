#include "kie_context.hpp"

int main(){
    kie::context ctx(10);
    ctx.get_one();
    std::thread([&]{
        std::this_thread::sleep_for(std::chrono::seconds(3));
        ctx.stop();
    }).detach();
    ctx.run();
    return 0;
}