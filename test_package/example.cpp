#include <td/telegram/Client.h>
#include <td/telegram/td_api.h>
#include <td/telegram/td_api.hpp>

namespace td_api = td::td_api;

int main() {
    td::Client::execute({0, td_api::make_object<td_api::setLogVerbosityLevel>(1)});
}
