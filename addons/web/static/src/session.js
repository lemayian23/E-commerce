/** @ecommerce-module **/

export const session = ecommerce.__session_info__ || {};
delete ecommerce.__session_info__;
