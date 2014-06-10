from dashboard.utils.i18n import get_text
logs_information = [
    #instance add && delete
    ['launch_instance', 'Instance Manage', 'add',
     'user %(user)s %(create_at)s created instance', 'true'],
    ['instance_delete', 'Instance Manage', 'del',
     'user %(user)s %(create_at)s deleted instance', 'true'],
    ['delete_instances', 'Instance Manage', 'del',
     'user %(user)s %(create_at)s batch deleted instance', 'true'],
    #instance action
    ['instance_reboot', 'Instance Manage', 'edit',
     'user %(user)s %(create_at)s reboot instance', 'true'],
    ['instance_pause', 'Instance Manage', 'edit',
     'user %(user)s %(create_at)s paused instance', 'false'],
    ['instance_unpause', 'Instance Manage', 'edit',
     'user %(user)s %(create_at)s unpaused instance', 'false'],
    ['instance_stop', 'Instance Manage', 'edit',
     'user %(user)s %(create_at)s stopped instance', 'true'],
    ['instance_unstop', 'Instance Manage', 'edit',
     'user %(user)s %(create_at)s unstopped instance', 'false'],
    ['change_pwd', 'Instance Manage', 'edit',
     'user %(user)s %(create_at)s changed password of instance', 'false'],
    ['update_instance', 'Instance Manage', 'edit',
     'user %(user)s %(create_at)s updated instance', 'false'],
    ['create_snapshot', 'Instance Manage', 'add',
     'user %(user)s %(create_at)s created snapshot', 'false'],
    ['restore_instance_data', 'Instance Manage', 'edit',
     'user %(user)s %(create_at)s restored instance data', 'false'],
    ['set_snapshot_public', 'Instance Manage', 'edit',
     'user %(user)s %(create_at)s set snapshot public', 'false'],
    #instance user
    ['distribution_instance_to_user', 'Instance Manage', 'add',
     'user %(user)s%(create_at)s add user to instance', 'false'],
    ['delete_distribution', 'Instance Manage', 'del',
     'user %(user)s %(create_at)s deleted user from instance', 'false'],
    # instance classify
    ['select_instance_classify', 'Instance Manage', 'add',
     get_text('user %(user)s %(create_at)s create instance classify'), 'false'],
    ['instance_flavor_update', 'Instance Manage', 'edit',
     get_text('user %(user)s %(create_at)s updated instance flavor'), 'false'],
    ['instance_classify_update_action', 'Instance Manage', 'edit',
     get_text('user %(user)sr %(create_at)s update instance classify'), 'false'],
    ['instance_classify_delete_action', 'Instance Manage', 'del',
     get_text('user %(user)s %(create_at)s deleted instance classify'), 'false'],
    ['instance_classify_action', 'Instance Manage', 'add',
     get_text('user %(user)s %(create_at)s created instance classify'), 'false'],
    ['classify_update_action', 'Instance Manage', 'edit',
     get_text('user %(user)sr %(create_at)s edit instance classify'), 'false'],
]
