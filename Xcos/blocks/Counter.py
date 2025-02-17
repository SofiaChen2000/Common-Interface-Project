def Counter(outroot, attribid, ordering, geometry, parameters):
    func_name = 'Counter'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'counter', 'C_OR_FORTRAN',
                         func_name, BLOCKTYPE_C)

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_Counter(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = 'Counter\n' + parameters[0] + " --> " + parameters[1]

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
