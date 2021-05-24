
from NENV import *

import _aix_support


class NodeBase(Node):
    pass


class _Aix_Bgt_Node(NodeBase):
    """
    """
    
    title = '_aix_bgt'
    type_ = '_aix_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _aix_support._aix_bgt())
        

class _Aix_Bosmp64_Node(NodeBase):
    """
    
    Return a Tuple[str, int] e.g., ['7.1.4.34', 1806]
    The fileset bos.mp64 is the AIX kernel. It's VRMF and builddate
    reflect the current ABI levels of the runtime environment.
    """
    
    title = '_aix_bosmp64'
    type_ = '_aix_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _aix_support._aix_bosmp64())
        

class _Aix_Tag_Node(NodeBase):
    """
    """
    
    title = '_aix_tag'
    type_ = '_aix_support'
    init_inputs = [
        NodeInputBP(label='vrtl'),
        NodeInputBP(label='bd'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _aix_support._aix_tag(self.input(0), self.input(1)))
        

class _Aix_Vrtl_Node(NodeBase):
    """
    """
    
    title = '_aix_vrtl'
    type_ = '_aix_support'
    init_inputs = [
        NodeInputBP(label='vrmf'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _aix_support._aix_vrtl(self.input(0)))
        

class Aix_Buildtag_Node(NodeBase):
    """
    
    Return the platform_tag of the system Python was built on.
    """
    
    title = 'aix_buildtag'
    type_ = '_aix_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _aix_support.aix_buildtag())
        

class Aix_Platform_Node(NodeBase):
    """
    
    AIX filesets are identified by four decimal values: V.R.M.F.
    V (version) and R (release) can be retreived using ``uname``
    Since 2007, starting with AIX 5.3 TL7, the M value has been
    included with the fileset bos.mp64 and represents the Technology
    Level (TL) of AIX. The F (Fix) value also increases, but is not
    relevant for comparing releases and binary compatibility.
    For binary compatibility the so-called builddate is needed.
    Again, the builddate of an AIX release is associated with bos.mp64.
    AIX ABI compatibility is described  as guaranteed at: https://www.ibm.com/    support/knowledgecenter/en/ssw_aix_72/install/binary_compatability.html

    For pep425 purposes the AIX platform tag becomes:
    "aix-{:1x}{:1d}{:02d}-{:04d}-{}".format(v, r, tl, builddate, bitsize)
    e.g., "aix-6107-1415-32" for AIX 6.1 TL7 bd 1415, 32-bit
    and, "aix-6107-1415-64" for AIX 6.1 TL7 bd 1415, 64-bit
    """
    
    title = 'aix_platform'
    type_ = '_aix_support'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, _aix_support.aix_platform())
        


export_nodes(
    _Aix_Bgt_Node,
    _Aix_Bosmp64_Node,
    _Aix_Tag_Node,
    _Aix_Vrtl_Node,
    Aix_Buildtag_Node,
    Aix_Platform_Node,
)
