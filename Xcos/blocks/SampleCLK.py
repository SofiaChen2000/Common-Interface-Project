def SampleCLK(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SampleCLK'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'sampleclk', 'DEFAULT',
                         func_name, BLOCKTYPE_D)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_SampleCLK(cell):
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
