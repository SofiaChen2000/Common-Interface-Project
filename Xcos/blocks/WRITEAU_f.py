def WRITEAU_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'WRITEAU_f'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'writeau', 'TYPE_2',
                         func_name, BLOCKTYPE_D,
                         dependsOnU='1')

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_WRITEAU_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
